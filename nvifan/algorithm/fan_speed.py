# -*- coding: utf-8 -*-

from typing import List


def get_speed_by_float(speed: float) -> int:
    """Get fan speed by float value."""
    if speed < 30:
        return 30
    if speed > 100:
        return 100
    return int(speed)


class FanSpeedLiner:
    current_speed: int

    def __init__(self, temperature_points: List[int], speeds: List[int]):
        if len(temperature_points) != len(speeds):
            raise ValueError(
                "The length of temperature_points and speeds must be the same."
            )

        self.min_speed = 30
        self.max_speed = 100

        self.current_speed = 0

        self.temperature_points = sorted(temperature_points)
        self.speeds = [
            max(self.min_speed, min(speed, self.max_speed)) for speed in speeds
        ]

    def get_speed(self, temperature: int) -> int:
        if temperature <= self.temperature_points[0]:
            return self.speeds[0]
        elif temperature >= self.temperature_points[-1]:
            return self.speeds[-1]

        for i in range(len(self.temperature_points) - 1):
            if (
                self.temperature_points[i]
                <= temperature
                < self.temperature_points[i + 1]
            ):
                # 使用线性插值计算速度
                slope = (self.speeds[i + 1] - self.speeds[i]) / (
                    self.temperature_points[i + 1] - self.temperature_points[i]
                )
                interpolated_speed = self.speeds[i] + slope * (
                    temperature - self.temperature_points[i]
                )
                return max(self.min_speed, min(int(interpolated_speed), self.max_speed))

    def get_final_speed(self, temperature: int) -> int:
        """Get final speed by temperature."""
        return get_speed_by_float(self.get_speed(temperature))

    def new_temperature(self, temperature: int) -> bool:
        new_speed = self.get_final_speed(temperature)
        if self.current_speed != new_speed:
            self.current_speed = new_speed
            return True
        else:
            return False


if __name__ == "__main__":
    print("Test Speed Calc")

    temperature_points = [40, 50, 60, 72]
    speeds = [30, 60, 80, 100]
    fan_speed_liner = FanSpeedLiner(temperature_points, speeds)

    # 获取某个温度下的风扇速度
    speed_at_55 = fan_speed_liner.get_speed(40)
    print(f"Speed at 55°C: {speed_at_55}%")
