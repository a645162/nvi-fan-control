# -*- coding: utf-8 -*-
from typing import List

from nvitop import Device, CudaDevice


def get_device_list() -> List[CudaDevice]:
    cuda_visible_devices = Device.cuda.all()
    return cuda_visible_devices


def get_device_name(device: CudaDevice) -> str:
    nvidia_snapshot = device.as_snapshot()
    return nvidia_snapshot['name']


def get_temperature(device: CudaDevice) -> int:
    nvidia_snapshot = device.as_snapshot()
    return nvidia_snapshot['temperature']


if __name__ == '__main__':
    devices = get_device_list()
    for device in devices:
        print(f"Device: {get_device_name(device)}, Temperature: {get_temperature(device)}")
