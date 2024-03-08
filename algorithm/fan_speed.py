def get_speed_by_float(speed: float) -> int:
    """Get fan speed by float value."""
    if speed < 30:
        return 30
    if speed > 100:
        return 100
    return int(speed)



if __name__=='__main__':
    print("Test Speed Calc")
    