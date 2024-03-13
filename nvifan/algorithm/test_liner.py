from .fan_speed import FanSpeedLiner


def test_fan_speed_liner():
    temperature_points = [40, 50, 60, 72]
    speeds = [30, 60, 80, 100]
    fan_speed_liner = FanSpeedLiner(temperature_points, speeds)

    assert fan_speed_liner.get_speed(30) == 30
    for i in range(0, 100):
        assert 30 <= fan_speed_liner.get_speed(i) <= 100
