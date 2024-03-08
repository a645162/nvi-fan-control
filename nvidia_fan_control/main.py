from nvidia_fan_control.monitor.temperature_monitor import start_temperature_monitor


def main():
    print("NVIDIA GPU Temperature Monitor")

    start_temperature_monitor()


if __name__ == '__main__':
    main()
