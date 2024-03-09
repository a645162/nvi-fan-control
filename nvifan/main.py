# -*- coding: utf-8 -*-

from nvifan.monitor.temperature_monitor import start_temperature_monitor
from nvifan.utils.permission import check_sudo


def main():
    print("NVIDIA GPU Temperature Monitor and Fan Auto Control for Linux")

    if not check_sudo():
        print("Please run this program as root")
        exit(-1)

    if not start_temperature_monitor():
        print("No NVIDIA GPU found")
        exit(1)


if __name__ == '__main__':
    main()
