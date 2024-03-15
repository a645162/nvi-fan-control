# -*- coding: utf-8 -*-

from nvifan.monitor.temperature_monitor import start_temperature_monitor
from nvifan.utils.permission import check_sudo

from nvifan.utils.logs import get_logger

logger = get_logger()


def main():
    print("NVIDIA GPU Temperature Monitor and Fan Auto Control for Linux")

    if not check_sudo():
        logger.error("Please run this program as root.")
        exit(-1)

    if not start_temperature_monitor():
        logger.error("No NVIDIA GPU found.")

        # Exit with code 0 to prevent automatic restart on failure
        exit(0)
        # To ensure that the service exits gracefully
        # to prevent automatic restart on failure
        # and avoid repeated restarts that consume resources.


if __name__ == "__main__":
    main()
