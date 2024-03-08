from typing import List


def get_speed_by_float(speed: float) -> int:
    """Get fan speed by float value."""
    if speed < 30:
        return 30
    if speed > 100:
        return 100
    return int(speed)


from typing import List


class FanSpeedLiner:
    def __init__(self, temperature_points: List[int], speeds: List[int]):
        if len(temperature_points) != len(speeds):
            raise ValueError("The length of temperature_points and speeds must be the same.")

        self.min_speed = 30
        self.max_speed = 100

        self.temperature_points = sorted(temperature_points)
        self.speeds = [max(self.min_speed, min(speed, self.max_speed)) for speed in speeds]

    def get_speed(self, temperature: int) -> int:
        if temperature <= self.temperature_points[0]:
            return self.speeds[0]
        elif temperature >= self.temperature_points[-1]:
            return self.speeds[-1]

        for i in range(len(self.temperature_points) - 1):
            if self.temperature_points[i] <= temperature < self.temperature_points[i + 1]:
                # 使用线性插值计算速度
                slope = (self.speeds[i + 1] - self.speeds[i]) / (
                        self.temperature_points[i + 1] - self.temperature_points[i]
                )
                interpolated_speed = self.speeds[i] + slope * (temperature - self.temperature_points[i])
                return max(self.min_speed, min(int(interpolated_speed), self.max_speed))


if __name__ == '__main__':
    print("Test Speed Calc")

    temperature_points = \
        [40, 50, 60, 72]
    speeds = \
        [30, 60, 80, 100]
    fan_speed_liner = FanSpeedLiner(temperature_points, speeds)

    # 获取某个温度下的风扇速度
    speed_at_55 = fan_speed_liner.get_speed(40)
    print(f"Speed at 55°C: {speed_at_55}%")
