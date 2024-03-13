# -*- coding: utf-8 -*-

from nvifan.utils.command import do_command
from nvifan.algorithm.fan_speed import get_speed_by_float
from nvifan.utils.logs import get_logger

logger = get_logger()


def nvidia_setting_command(command: str):
    ret = do_command(f"nvidia-settings -a {command} -c display")
    if ret[0] != 0:
        logger.error(f"[{ret[0]}] {command}")
        logger.error(f"{ret[1]}")
    else:
        logger.info(f"[{ret[0]}] {command}")


def set_fan_speed(fan_id: int, speed: float):
    final_speed = get_speed_by_float(speed)
    command = f"[fan:{fan_id}]/GPUTargetFanSpeed={final_speed}"

    nvidia_setting_command(command=command)


def restore_auto_mode(gpu_id: int):
    command = f"[gpu:{gpu_id}]/GPUFanControlState=0"

    nvidia_setting_command(command=command)


def test_speed_control():
    # set_fan_speed(0, 100)

    restore_auto_mode(0)


if __name__ == "__main__":
    print("NVIDIA Fan Control Test")

    test_speed_control()
