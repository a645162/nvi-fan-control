#!/usr/bin/env python3
import re
import time
import argparse
from subprocess import TimeoutExpired, check_output, Popen, PIPE, STDOUT
from tempfile import mkdtemp
from contextlib import contextmanager

parser = argparse.ArgumentParser(description=r'''
GPU fan control for Linux.

By default, this uses a clamped linear fan curve, going from 30% below 55C to 99%
above 80C. There's also a small hysteresis gap, because _changes_ in fan noise
are a lot more distracting than steady fan noise.

I can't claim it's optimal, but it Works For My Machine (TM). Full load is about
75C and 80%.
''')
parser.add_argument('--temp', nargs='+', default=[55, 80], type=float, help='The temperature ranges where the fan speed will increase linearly')
parser.add_argument('--speed', nargs='+', default=[30, 99], type=float, help='The fan speed ranges')
parser.add_argument('--hyst', nargs='?', default=2, type=float, help='The hysteresis gap. Large gaps will reduce how often the fan speed is changed, but might mean the fan runs faster than necessary')
parser.add_argument('--kill', action='store_true', default=False, help='Whether to kill existing Xorg sessions')
parser.add_argument('--verbose', action='store_true', default=False, help='Whether to print extra debugging information')
parser.add_argument('--debug', action='store_true', default=False, help='Whether to only start the Xorg subprocesses, and not actually alter the fan speed. This can be useful for debugging.')
args = parser.parse_args()

T_HYST =  args.hyst

assert len(args.temp) == len(args.speed), 'temp and speed should have the same length'
assert len(args.temp) >= 2, 'Please use at least two points for temp'
assert len(args.speed) >= 2, 'Please use at least two points for speed'

def log_output(command, ok=(0,)):
    output = []
    if args.verbose:
        print('Command launched: ' + ' '.join(command))
    p = Popen(command, stdout=PIPE, stderr=STDOUT)
    try:
        p.wait(60)
        for line in p.stdout:
            output.append(line.decode().strip())
            if args.verbose:
                print(line.decode().strip())
        if args.verbose:
            print('Command finished')
    except TimeoutExpired:
        print('Command timed out: ' + ' '.join(command))
        raise
    finally:
        if p.returncode not in ok:
            print('\n'.join(output))
            raise ValueError('Command crashed with return code ' + str(p.returncode) + ': ' + ' '.join(command))
        return '\n'.join(output)

def decimalize(bus):
    """Converts a bus ID to an xconf-friendly format by dropping the domain and converting each hex component to
    decimal"""
    return ':'.join([str(int('0x' + p, 16)) for p in re.split('[:.]', bus[9:])])

def gpu_buses():
    return log_output(['nvidia-smi', '--format=csv,noheader', '--query-gpu=pci.bus_id']).splitlines()

def query(bus, field):
    [line] = log_output(['nvidia-smi', '--format=csv,noheader', '--query-gpu='+field, '-i', bus]).splitlines()
    return line

def temperature(bus):
    return int(query(bus, 'temperature.gpu'))

def determine_segment(t):
    '''Determines which piece (segment) of a user-specified piece-wise function
    t belongs to. For example:
        args.temp = [30, 50, 70, 90]
        (segment 0) 30 (0 segment) 50 (1 segment) 70 (2 segment) 90 (segment 2)
        args.speed = [10, 30, 50, 75]
        (segment 0) 10 (0 segment) 30 (1 segment) 50 (2 segment) 75 (segment 2)'''
    # TODO: assert temps and speeds are sorted
    # the loop exits when:
    #   a) t is less than the min temp (returns: segment 0)
    #   b) t belongs to a segment (returns: the segment)
    #   c) t is higher than the max temp (return: the last segment)
    segments = zip(
            args.temp[:-1], args.temp[1:],
            args.speed[:-1], args.speed[1:])
    for temp_a, temp_b, speed_a, speed_b in segments:
        if t < temp_a:
            break
        if temp_a <= t < temp_b:
            break
    return temp_a, temp_b, speed_a, speed_b

def min_speed(t):
    temp_a, temp_b, speed_a, speed_b = determine_segment(t)
    load = (t - temp_a)/float(temp_b - temp_a)
    return int(min(max(speed_a + (speed_b - speed_a)*load, speed_a), speed_b))

def max_speed(t):
    return min_speed(t + T_HYST)

def target_speed(s, t):
    l, u = min_speed(t), max_speed(t)
    return min(max(s, l), u), l, u

def assign(display, command):
    # Our duct-taped-together xorg.conf leads to some innocent - but voluminous - warning messages about
    # failing to authenticate. Here we dispose of them
    log_output(['nvidia-settings', '-a', command, '-c', display])


def set_speed(display, target):
    # toggle all fans
    output = log_output(['nvidia-settings', '-q', 'fans', '-c', 'display'])
    fans = int(re.search(r"^([0-9].*)\sFan", output.strip().split("\n")[0]).group(1))

    for fanId in range(fans):
        assign(display, f'[fan:{fanId}]/GPUTargetFanSpeed='+str(int(target)))

def manage_fans(displays):
    """Launches an X server for each GPU, then continually loops over the GPU fans to set their speeds according
    to the GPU temperature. When interrupted, it releases the fan control back to the driver and shuts down the
    X servers"""
    output = log_output(['nvidia-settings', '-q', 'gpus', '-c', 'display'])
    gpus = int(re.search(r"^([0-9].*)\sGPU", output.strip().split("\n")[0]).group(1))

    try:
        # turn on all gpu fans speed control
        for bus, display in displays.items():
            for gpuId in range(gpus): assign(display, f'[gpu:{gpuId}]/GPUFanControlState=1')
            print('Gain fan speed control for GPU at DISPLAY'+display)
        speeds = {b: 0 for b in displays}
        while True:
            for bus, display in displays.items():
                temp = temperature(bus)
                s, l, u = target_speed(speeds[bus], temp)
                if s != speeds[bus]:
                    print('GPU {}, {}C -> [{}%-{}%]. Setting speed to {}%'.format(display, temp, l, u, s))
                    set_speed(display,  s)
                    speeds[bus] = s
                else:
                    print('GPU {}, {}C -> [{}%-{}%]. Leaving speed at {}%'.format(display, temp, l, u, s))
            time.sleep(5)
    finally:
        # release all gpu fans speed control
        for bus, display in displays.items():
            for gpuId in range(gpus): assign(display, f'[gpu:{gpuId}]/GPUFanControlState=0')
            print('Released fan speed control for GPU at DISPLAY'+display)

def debug_loop(displays):
    displays = '\n'.join(str(d) + ' - ' + str(b) for b, d in displays.items())
    print('\n\n\nLOOPING IN DEBUG MODE. DISPLAYS ARE:\n' + displays + '\n\n\n')
    while True:
        print('Looping in debug mode')
        time.sleep(5)


def run():
    buses = gpu_buses()
    with xservers(buses) as displays:
        if args.debug:
            debug_loop(displays)
        else:
            manage_fans(displays)

if __name__ == '__main__':
    run()
