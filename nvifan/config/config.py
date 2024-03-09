# -*- coding: utf-8 -*-

from nvifan.utils.yaml_parser import parse_yaml

start_temperature = 50

temperature_points = \
    [30, 50, 60, 70]
speeds = \
    [30, 60, 80, 100]

time_interval = 10


def read_config(yaml_path: str):
    yaml_dict: dict = parse_yaml(yaml_path)
    print(yaml_dict)

    global start_temperature, temperature_points, speeds

    if 'start_temperature' in yaml_dict:
        start_temperature = yaml_dict['start_temperature']

    if 'temperature_points' in yaml_dict:
        yaml_temperature_points = yaml_dict['temperature_points']
        if isinstance(yaml_temperature_points, list):
            temperature_points = yaml_temperature_points
        else:
            raise ValueError('temperature_points should be a list')

    if 'speeds' in yaml_dict:
        yaml_speeds = yaml_dict['speeds']
        if isinstance(yaml_speeds, list):
            speeds = yaml_speeds
        else:
            raise ValueError('speeds should be a list')

    if 'time_interval' in yaml_dict:
        time_interval = yaml_dict['time_interval']
        if not isinstance(time_interval, int):
            if isinstance(time_interval, str):
                try:
                    time_interval = int(time_interval)
                except:
                    raise ValueError('time_interval should be a int')
            else:
                raise ValueError('time_interval should be a int')


if __name__ == '__main__':
    read_config('config.yaml')
