# -*- coding: utf-8 -*-

import threading

from nvitop import NaType

from nvifan.nvi.device_list import *
from nvifan.config import config
from time import sleep as time_sleep
from typing import List
from nvifan.algorithm.fan_speed import FanSpeedLiner
from nvifan.nvi.fan_control import set_fan_speed, restore_auto_mode

thread_list: List[threading.Thread] = []


class TemperatureMonitorThread(threading.Thread):
    device: CudaDevice
    device_name: str
    device_index: int

    start_temperature: int

    temperature_points: List[int]
    speeds: List[int]

    time_interval: int

    fanSpeedLiner: FanSpeedLiner

    controlling: bool

    def __init__(
            self,
            device: CudaDevice,
            start_temperature: int,
            temperature_points: List[int],
            speeds: List[int],
            time_interval: int
    ):
        threading.Thread.__init__(self)

        self.device = device
        self.device_name = get_device_name(device)
        self.device_index = get_device_index(device)

        self.start_temperature = start_temperature

        self.temperature_points = temperature_points
        self.speeds = speeds
        self.fanSpeedLiner = FanSpeedLiner(temperature_points, speeds)

        self.time_interval = time_interval

        self.controlling = False

        print(
            "[{}]{} Start temperature monitor".format(
                self.device_index,
                self.device_name
            )
        )
        print(
            "[{}]Start controlling temperature: {}".format(
                self.device_index,
                self.start_temperature
            )
        )
        print(
            "[{}]Temperature points: {}".format(
                self.device_index,
                self.temperature_points
            )
        )
        print(
            "[{}]Speeds: {}".format(
                self.device_index,
                self.speeds
            )
        )
        print(
            "[{}]Time interval: {}".format(self.device_index, self.time_interval)
        )

    def get_now_temperature(self):
        return get_temperature(self.device)

    def run(self):
        while True:
            now_temperature = self.get_now_temperature()

            is_need_control = now_temperature > self.start_temperature

            if is_need_control and not self.controlling:
                self.controlling = True
                print(
                    "[{}]{} Start controlling".format(
                        self.device_index,
                        self.device_name
                    )
                )
            elif not is_need_control and self.controlling:
                self.controlling = False
                print(
                    "[{}]{} Stop controlling".format(
                        self.device_index,
                        self.device_name
                    )
                )
                restore_auto_mode(self.device_index)

            if is_need_control:
                if self.fanSpeedLiner.new_temperature(now_temperature):
                    new_speed: int = self.fanSpeedLiner.current_speed
                    set_fan_speed(self.device_index, new_speed)
                    print(
                        "[{}]{}C->{}%".format(
                            self.device_index,
                            now_temperature,
                            new_speed
                        )
                    )

            time_sleep(self.time_interval)


def start_temperature_monitor() -> bool:
    device_list = get_device_list()

    for device in device_list:
        if isinstance(device.fan_speed(), NaType):
            print(
                "[{}]{} does not have Fan!(Pass)".format(
                    get_device_index(device),
                    get_device_name(device)
                )
            )

            continue

        thread = TemperatureMonitorThread(
            device,
            config.start_temperature,
            config.temperature_points,
            config.speeds,
            config.time_interval
        )
        thread.start()
        thread_list.append(thread)

    for thread in thread_list:
        thread.join()

    if len(thread_list) == 0:
        return False


if __name__ == "__main__":
    start_temperature_monitor()
