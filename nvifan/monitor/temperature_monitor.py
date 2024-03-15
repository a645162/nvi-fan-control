# -*- coding: utf-8 -*-

from typing import List, Any
import signal
import sys
import threading
from time import sleep as time_sleep

from nvitop import NaType, CudaDevice

# Program Configure
from nvifan.config import config

# Fan Control Algorithm
from nvifan.algorithm.fan_speed import FanSpeedLiner

# Device Info
from nvifan.nvi.device_list import get_device_name, get_device_index, get_temperature
from nvifan.nvi.device_list import get_device_list

# Device Control
from nvifan.nvi.fan_control import set_fan_speed, restore_auto_mode

# Program Logs
from nvifan.utils.logs import get_logger

logger = get_logger()


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
        time_interval: int,
    ):
        threading.Thread.__init__(self)

        self.continue_run = True

        self.device = device
        self.device_name = get_device_name(device)
        self.device_index = get_device_index(device)

        self.start_temperature = start_temperature

        self.temperature_points = temperature_points
        self.speeds = speeds
        self.fanSpeedLiner = FanSpeedLiner(temperature_points, speeds)

        self.time_interval = time_interval

        self.controlling = False

        logger.info(
            "[{}]{} Start temperature monitor".format(
                self.device_index, self.device_name
            )
        )
        logger.info(
            "[{}]Start controlling temperature: {}".format(
                self.device_index, self.start_temperature
            )
        )
        logger.info(
            "[{}]Temperature points: {}".format(
                self.device_index, self.temperature_points
            )
        )
        logger.info("[{}]Speeds: {}".format(self.device_index, self.speeds))
        logger.info(
            "[{}]Time interval: {}".format(self.device_index, self.time_interval)
        )

    def restore_current_to_auto_mode(self):
        restore_auto_mode(self.device_index)

    def get_now_temperature(self):
        return get_temperature(self.device)

    def run(self):
        while self.continue_run:
            now_temperature = self.get_now_temperature()

            is_need_control = now_temperature > self.start_temperature

            if is_need_control and not self.controlling:
                self.controlling = True
                logger.info(
                    "[{}]{} Start controlling".format(
                        self.device_index, self.device_name
                    )
                )
            elif not is_need_control and self.controlling:
                self.controlling = False
                logger.info(
                    "[{}]{} Stop controlling".format(
                        self.device_index, self.device_name
                    )
                )
                self.restore_current_to_auto_mode()

            if is_need_control and self.continue_run:
                if self.fanSpeedLiner.new_temperature(now_temperature):
                    new_speed: int = self.fanSpeedLiner.current_speed
                    set_fan_speed(self.device_index, new_speed)
                    # logger.info(
                    #     "[{}] Temperature {}C -> Speed {}%".format(
                    #         self.device_index, now_temperature, new_speed
                    #     )
                    # )

            time_sleep(self.time_interval)


thread_list: List[TemperatureMonitorThread] = []


def signal_handler(signal: int, frame: Any) -> None:
    logger.info("Received signal: {}".format(signal))
    for thread in thread_list:
        thread.continue_run = False
        if hasattr(thread, "restore_current_to_auto_mode"):
            thread.restore_current_to_auto_mode()

    sys.exit(0)


def start_temperature_monitor() -> bool:
    device_list = get_device_list()

    for device in device_list:
        if isinstance(device.fan_speed(), NaType):
            logger.exception(
                "[{}]{} does not have Fan!(Pass)".format(
                    get_device_index(device), get_device_name(device)
                )
            )

            continue

        thread = TemperatureMonitorThread(
            device,
            config.start_temperature,
            config.temperature_points,
            config.speeds,
            config.time_interval,
        )
        logger.info(
            "[{}]{} Thread Created.".format(
                get_device_index(device), get_device_name(device)
            )
        )
        thread.start()
        logger.info(
            "[{}]{} Thread Started.".format(
                get_device_index(device), get_device_name(device)
            )
        )
        thread_list.append(thread)

    # Register the signal handler
    # Ctrl+C
    signal.signal(signal.SIGINT, signal_handler)
    # Terminate(Such as "systemctl stop nvifan")
    signal.signal(signal.SIGTERM, signal_handler)

    for thread in thread_list:
        thread.join()
        if hasattr(thread, "restore_current_to_auto_mode"):
            thread.restore_current_to_auto_mode()

    logger.info("All Monitor Threads Stopped.")

    return len(thread_list) != 0


if __name__ == "__main__":
    start_temperature_monitor()
