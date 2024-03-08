from setuptools import setup, find_packages

setup(
    name="NVIDIA-Fan-Control",
    version="0.1",
    description="NVIDIA GPU fan control for Linux",
    url="https://github.com/a645162/nvidia-fan-control",
    author="Haomin Kong",
    author_email="a645162@gmail.com",
    license="GPL-3",
    packages=find_packages(),  # 自动找到项目中的所有包
    install_requires=[  # 依赖的库列表
        "nvitop",
    ],
    entry_points={  # 如果你的项目有命令行工具，可以在这里设置
        "console_scripts": [
            "nvidia-fan-control = your_package.main:main",  # 示例，请替换成实际的入口点
        ],
    },
    scripts=["scripts/your_script.py"],  # 可执行脚本，如果需要的话
)
