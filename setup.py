from setuptools import setup, find_packages

# read the contents of your README file
from pathlib import Path

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name="nvifan",
    version="0.2.1",
    description="NVIDIA GPU fan control for Linux",
    long_description=long_description,
    long_description_content_type='text/markdown',
    url="https://github.com/a645162/nvidia-fan-control",
    author="Haomin Kong",
    author_email="a645162@gmail.com",
    license="GPLv3",
    packages=find_packages(),  # 自动找到项目中的所有包
    install_requires=[  # 依赖的库列表
        "nvitop",
        "chardet",
        "PyYaml"
    ],
    entry_points={
        "console_scripts": [
            "nvifan = nvifan.main:main",
            "nvifan-install = nvifan.tools.installer:install",
            "nvifan-uninstall = nvifan.tools.installer:uninstall",
        ],
    },
)
