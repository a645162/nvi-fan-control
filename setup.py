# read the contents of your README file
from pathlib import Path

from setuptools import setup, find_packages

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

__version__ = "1.2.1"

url_github_main_readme_zh_cn = \
    r'https://github.com/a645162/nvi-fan-control/blob/main/README.zh-CN.md'
long_description = long_description.replace(
    "(README.zh-CN.md)",
    f"({url_github_main_readme_zh_cn})"
)

setup(
    name="nvifan",
    version=__version__,
    description="NVIDIA GPU fan control for Linux",
    long_description=long_description,
    long_description_content_type='text/markdown',
    url="https://github.com/a645162/nvidia-fan-control",
    author="Haomin Kong",
    author_email="a645162@gmail.com",
    license="GPLv3",
    packages=find_packages(),
    python_requires=">=3.7",
    install_requires=[
        "nvitop",
        "chardet",
        "PyYaml",
        "loguru"
    ],
    entry_points={
        "console_scripts": [
            "nvifan = nvifan.main:main",
            "nvifan-install = nvifan.tools.installer:install",
            "nvifan-uninstall = nvifan.tools.installer:uninstall",
        ],
    },
)
