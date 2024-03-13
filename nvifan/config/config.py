# -*- coding: utf-8 -*-

import argparse
import os

from nvifan.utils.yaml_parser import parse_yaml

from nvifan.utils.logs import get_logger

logger = get_logger()

parser = argparse.ArgumentParser(description="Command line argument parser")
parser.add_argument(
    "--start_temperature", "-s", type=int, default=50, help="Starting temperature"
)

parser.add_argument(
    "--temperature_points",
    "-t",
    nargs="+",
    type=int,
    default=[30, 50, 60, 70],
    help="List of temperature points",
)

parser.add_argument(
    "--speeds",
    "-v",
    nargs="+",
    type=int,
    default=[30, 60, 80, 100],
    help="List of speeds",
)

parser.add_argument("--time_interval", "-i", type=int, default=10, help="Time interval")

parser.add_argument(
    "--yaml", "-y", type=str, default="/etc/nvifan.yaml", help="YAML config file path"
)

args = parser.parse_args()

yaml_file_path = args.yaml.strip()

start_temperature = args.start_temperature
temperature_points = args.temperature_points
speeds = args.speeds
time_interval = args.time_interval


def read_config(yaml_path: str):
    yaml_dict: dict = parse_yaml(yaml_path)
    print(yaml_dict)

    global start_temperature, temperature_points, speeds, time_interval

    if "start_temperature" in yaml_dict:
        start_temperature = yaml_dict["start_temperature"]

    if "temperature_points" in yaml_dict:
        yaml_temperature_points = yaml_dict["temperature_points"]
        if isinstance(yaml_temperature_points, list):
            temperature_points = yaml_temperature_points
        else:
            raise ValueError("temperature_points should be a list")

    if "speeds" in yaml_dict:
        yaml_speeds = yaml_dict["speeds"]
        if isinstance(yaml_speeds, list):
            speeds = yaml_speeds
        else:
            raise ValueError("speeds should be a list")

    if "time_interval" in yaml_dict:
        new_time_interval = yaml_dict["time_interval"]
        if not isinstance(new_time_interval, int):
            if isinstance(new_time_interval, str):
                try:
                    time_interval = int(new_time_interval)
                except:
                    raise ValueError("time_interval should be a int")
            else:
                raise ValueError("time_interval should be a int")


if len(yaml_file_path) > 0 and os.path.exists(yaml_file_path):
    print("Read configure from file: ", yaml_file_path)
    read_config(yaml_file_path)


def save_yaml(path: str):
    conf_dict: dict = {
        "start_temperature": start_temperature,
        "temperature_points": temperature_points,
        "speeds": speeds,
        "time_interval": time_interval,
    }
    # Convert Dict to Yaml
    import yaml

    yaml_str = yaml.dump(conf_dict)
    # Write to file
    with open(path, "w", encoding="utf-8") as file:
        file.write(yaml_str)


if __name__ == "__main__":
    read_config("config_template.yaml")
    save_yaml("config_save.yaml")
