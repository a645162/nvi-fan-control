# NVIFAN

<!-- markdownlint-disable html -->

![Python 3.7+](https://img.shields.io/badge/Python-3.7%2B-brightgreen)
[![PyPI](https://img.shields.io/pypi/v/nvifan?label=pypi&logo=pypi)](https://pypi.org/project/nvifan)
[![Python Package using Conda](https://github.com/a645162/nvi-fan-control/actions/workflows/python-package-conda.yaml/badge.svg)](https://github.com/a645162/nvi-fan-control/actions/workflows/python-package-conda.yaml)
[![Upload Python Package](https://github.com/a645162/nvi-fan-control/actions/workflows/python-publish.yaml/badge.svg)](https://github.com/a645162/nvi-fan-control/actions/workflows/python-publish.yaml)
[![GitHub Repo Stars](https://img.shields.io/github/stars/a645162/nvi-fan-control?label=stars&logo=github&color=brightgreen)](https://github.com/a645162/nvi-fan-control/stargazers)
[![License](https://img.shields.io/github/license/a645162/nvi-fan-control?label=license&logo=data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAyNCAyNCIgd2lkdGg9IjI0IiBoZWlnaHQ9IjI0IiBmaWxsPSIjZmZmZmZmIj48cGF0aCBmaWxsLXJ1bGU9ImV2ZW5vZGQiIGQ9Ik0xMi43NSAyLjc1YS43NS43NSAwIDAwLTEuNSAwVjQuNUg5LjI3NmExLjc1IDEuNzUgMCAwMC0uOTg1LjMwM0w2LjU5NiA1Ljk1N0EuMjUuMjUgMCAwMTYuNDU1IDZIMi4zNTNhLjc1Ljc1IDAgMTAwIDEuNUgzLjkzTC41NjMgMTUuMThhLjc2Mi43NjIgMCAwMC4yMS44OGMuMDguMDY0LjE2MS4xMjUuMzA5LjIyMS4xODYuMTIxLjQ1Mi4yNzguNzkyLjQzMy42OC4zMTEgMS42NjIuNjIgMi44NzYuNjJhNi45MTkgNi45MTkgMCAwMDIuODc2LS42MmMuMzQtLjE1NS42MDYtLjMxMi43OTItLjQzMy4xNS0uMDk3LjIzLS4xNTguMzEtLjIyM2EuNzUuNzUgMCAwMC4yMDktLjg3OEw1LjU2OSA3LjVoLjg4NmMuMzUxIDAgLjY5NC0uMTA2Ljk4NC0uMzAzbDEuNjk2LTEuMTU0QS4yNS4yNSAwIDAxOS4yNzUgNmgxLjk3NXYxNC41SDYuNzYzYS43NS43NSAwIDAwMCAxLjVoMTAuNDc0YS43NS43NSAwIDAwMC0xLjVIMTIuNzVWNmgxLjk3NGMuMDUgMCAuMS4wMTUuMTQuMDQzbDEuNjk3IDEuMTU0Yy4yOS4xOTcuNjMzLjMwMy45ODQuMzAzaC44ODZsLTMuMzY4IDcuNjhhLjc1Ljc1IDAgMDAuMjMuODk2Yy4wMTIuMDA5IDAgMCAuMDAyIDBhMy4xNTQgMy4xNTQgMCAwMC4zMS4yMDZjLjE4NS4xMTIuNDUuMjU2Ljc5LjRhNy4zNDMgNy4zNDMgMCAwMDIuODU1LjU2OCA3LjM0MyA3LjM0MyAwIDAwMi44NTYtLjU2OWMuMzM4LS4xNDMuNjA0LS4yODcuNzktLjM5OWEzLjUgMy41IDAgMDAuMzEtLjIwNi43NS43NSAwIDAwLjIzLS44OTZMMjAuMDcgNy41aDEuNTc4YS43NS43NSAwIDAwMC0xLjVoLTQuMTAyYS4yNS4yNSAwIDAxLS4xNC0uMDQzbC0xLjY5Ny0xLjE1NGExLjc1IDEuNzUgMCAwMC0uOTg0LS4zMDNIMTIuNzVWMi43NXpNMi4xOTMgMTUuMTk4YTUuNDE4IDUuNDE4IDAgMDAyLjU1Ny42MzUgNS40MTggNS40MTggMCAwMDIuNTU3LS42MzVMNC43NSA5LjM2OGwtMi41NTcgNS44M3ptMTQuNTEtLjAyNGMuMDgyLjA0LjE3NC4wODMuMjc1LjEyNi41My4yMjMgMS4zMDUuNDUgMi4yNzIuNDVhNS44NDYgNS44NDYgMCAwMDIuNTQ3LS41NzZMMTkuMjUgOS4zNjdsLTIuNTQ3IDUuODA3eiI+PC9wYXRoPjwvc3ZnPgo=)](#license)

A tool aimed at controlling NVIDIA GPU fans on Linux.

[中文版README](README.zh-CN.md)

The program has been developed in Python, and its source code is conveniently hosted on GitHub.

Written by: [Haomin Kong](https://github.com/a645162)

If this program turns out to be beneficial for you,
kindly consider showing your support by starring it on GitHub.
Your recognition is greatly appreciated!

## Usage

### Install

```bash
pip install nvifan
```

### Direct Run

```bash
sudo nvifan
```

or

```bash
# Use 'su' to run as root
su
nvifan
```

#### Tips

* You can use `nvifan --help` to see the usage.
* (Not recommended)You can use `screen` or `tmux` to keep the program running when you close the terminal.

### Upgrade

We recommend using the official PyPI repository to upgrade the package.
The third party PyPI mirrors are used to improve the download speed.
But may an older version,so you can use this command to upgrade to the latest version.

```bash
pip install --upgrade nvifan -i https://pypi.python.org/simple
```

By the way, if you are using systemd,
you can use the following command to restart the service after upgrading.

```bash
sudo systemctl restart nvifan
```

### Install as Service(Recommended)

#### Install Service

```bash
sudo nvifan-install
```

### Uninstall Service

```bash
sudo nvifan-uninstall
```

## Install from Source

```bash
chmod +x install.sh
./install.sh
```

## Build Wheel

```bash
chmod +x build.sh
./build.sh
```

## Log

The log file is located at `/var/log/nvi/nvifan.log`.

If you want to view the log, you can use the following command:

```bash
sudo journalctl -u nvifan
```

or

```bash
cat /var/log/nvi/nvifan.log
```

If you want to report a bug, you should provide the log file.
You can make an `Issue` on GitHub and attach the log file.

## Gitee

We have a Gitee repository, which is a mirror of the GitHub repository.

[https://gitee.com/a645162/nvi-fan-control](https://gitee.com/a645162/nvi-fan-control)

This repository is used to improve the download speed in China.

**So that:**

- Please **do not** use this repository for development or make a `Pull Request`.
- Please **do not** make an `Issue` on Gitee, because we do not check the `Issue` on Gitee.

## Ref

Based on [CoolGPUs](https://github.com/andyljones/coolgpus) and [nvitop](https://github.com/XuehaiPan/nvitop).
Thanks for their work.
