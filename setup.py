from setuptools import setup, find_packages

setup(
    name="nvidia_fan_control",
    version="0.1",
    description="NVIDIA GPU fan control for Linux",
    url="https://github.com/a645162/nvidia-fan-control",
    author="Haomin Kong",
    author_email="a645162@gmail.com",
    license="GPL-3",
    packages=find_packages(),  # 自动找到项目中的所有包
    install_requires=[  # 依赖的库列表
        "nvitop",
        "chardet",
        "PyYaml"
    ],
    entry_points={
        "console_scripts": [
            "nvidia_fan_control = nvidia_fan_control.main:main",
        ],
    },
)
