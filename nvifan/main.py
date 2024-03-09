# -*- coding: utf-8 -*-

from nvifan.monitor.temperature_monitor import start_temperature_monitor


def main():
    print("NVIDIA GPU Temperature Monitor and Fan Auto Control for Linux")

    start_temperature_monitor()


if __name__ == '__main__':
    main()
