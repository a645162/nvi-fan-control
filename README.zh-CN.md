# NVIFAN

<!-- markdownlint-disable html -->

![Python 3.7+](https://img.shields.io/badge/Python-3.7%2B-brightgreen)
[![PyPI](https://img.shields.io/pypi/v/nvifan?label=pypi&logo=pypi)](https://pypi.org/project/nvifan)
[![Python Package using Conda](https://github.com/a645162/nvi-fan-control/actions/workflows/python-package-conda.yaml/badge.svg)](https://github.com/a645162/nvi-fan-control/actions/workflows/python-package-conda.yaml)
[![Upload Python Package](https://github.com/a645162/nvi-fan-control/actions/workflows/python-publish.yaml/badge.svg)](https://github.com/a645162/nvi-fan-control/actions/workflows/python-publish.yaml)
[![GitHub Repo Stars](https://img.shields.io/github/stars/a645162/nvi-fan-control?label=stars&logo=github&color=brightgreen)](https://github.com/a645162/nvi-fan-control/stargazers)
[![License](https://img.shields.io/github/license/a645162/nvi-fan-control?label=license&logo=data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAyNCAyNCIgd2lkdGg9IjI0IiBoZWlnaHQ9IjI0IiBmaWxsPSIjZmZmZmZmIj48cGF0aCBmaWxsLXJ1bGU9ImV2ZW5vZGQiIGQ9Ik0xMi43NSAyLjc1YS43NS43NSAwIDAwLTEuNSAwVjQuNUg5LjI3NmExLjc1IDEuNzUgMCAwMC0uOTg1LjMwM0w2LjU5NiA1Ljk1N0EuMjUuMjUgMCAwMTYuNDU1IDZIMi4zNTNhLjc1Ljc1IDAgMTAwIDEuNUgzLjkzTC41NjMgMTUuMThhLjc2Mi43NjIgMCAwMC4yMS44OGMuMDguMDY0LjE2MS4xMjUuMzA5LjIyMS4xODYuMTIxLjQ1Mi4yNzguNzkyLjQzMy42OC4zMTEgMS42NjIuNjIgMi44NzYuNjJhNi45MTkgNi45MTkgMCAwMDIuODc2LS42MmMuMzQtLjE1NS42MDYtLjMxMi43OTItLjQzMy4xNS0uMDk3LjIzLS4xNTguMzEtLjIyM2EuNzUuNzUgMCAwMC4yMDktLjg3OEw1LjU2OSA3LjVoLjg4NmMuMzUxIDAgLjY5NC0uMTA2Ljk4NC0uMzAzbDEuNjk2LTEuMTU0QS4yNS4yNSAwIDAxOS4yNzUgNmgxLjk3NXYxNC41SDYuNzYzYS43NS43NSAwIDAwMCAxLjVoMTAuNDc0YS43NS43NSAwIDAwMC0xLjVIMTIuNzVWNmgxLjk3NGMuMDUgMCAuMS4wMTUuMTQuMDQzbDEuNjk3IDEuMTU0Yy4yOS4xOTcuNjMzLjMwMy45ODQuMzAzaC44ODZsLTMuMzY4IDcuNjhhLjc1Ljc1IDAgMDAuMjMuODk2Yy4wMTIuMDA5IDAgMCAuMDAyIDBhMy4xNTQgMy4xNTQgMCAwMC4zMS4yMDZjLjE4NS4xMTIuNDUuMjU2Ljc5LjRhNy4zNDMgNy4zNDMgMCAwMDIuODU1LjU2OCA3LjM0MyA3LjM0MyAwIDAwMi44NTYtLjU2OWMuMzM4LS4xNDMuNjA0LS4yODcuNzktLjM5OWEzLjUgMy41IDAgMDAuMzEtLjIwNi43NS43NSAwIDAwLjIzLS44OTZMMjAuMDcgNy41aDEuNTc4YS43NS43NSAwIDAwMC0xLjVoLTQuMTAyYS4yNS4yNSAwIDAxLS4xNC0uMDQzbC0xLjY5Ny0xLjE1NGExLjc1IDEuNzUgMCAwMC0uOTg0LS4zMDNIMTIuNzVWMi43NXpNMi4xOTMgMTUuMTk4YTUuNDE4IDUuNDE4IDAgMDAyLjU1Ny42MzUgNS40MTggNS40MTggMCAwMDIuNTU3LS42MzVMNC43NSA5LjM2OGwtMi41NTcgNS44M3ptMTQuNTEtLjAyNGMuMDgyLjA0LjE3NC4wODMuMjc1LjEyNi41My4yMjMgMS4zMDUuNDUgMi4yNzIuNDVhNS44NDYgNS44NDYgMCAwMDIuNTQ3LS41NzZMMTkuMjUgOS4zNjdsLTIuNTQ3IDUuODA3eiI+PC9wYXRoPjwvc3ZnPgo=)](#license)

这个工具旨在帮助Linux系统用户控制NVIDIA GPU的风扇。

[English Version README](README.zh-CN.md)

这个程序是用Python精心编写的，源代码已经公开上传至GitHub平台，方便大家查阅与使用。

作者：[Haomin Kong](https://github.com/a645162)

如果你在使用这个程序的过程中发现它对你有所帮助，那么请不吝在GitHub上给予我一个小小的点赞（star）。
你的支持与认可对我来说意义非凡，非常感谢！

## 使用方法

### 安装

想安装这个工具吗？很简单，只需要在终端里输入以下命令：

```bash
pip install nvifan
```

### 直接运行

安装好了之后，就可以开始用了。你可以用管理员权限直接运行：

```bash
sudo nvifan
```

或者，如果你想先用 `su` 命令切换到 root 用户再运行，也可以：

```bash
su
nvifan
```

#### 小提示

* 想了解更多使用方法？那就输入 `nvifan --help` 看看吧。
* 不过提醒一下，虽然可以使用 `screen` 或 `tmux` 让程序在关闭终端后继续运行，但一般不推荐这么做。

### 升级

想要更新到这个工具的最新版本吗？
建议使用官方的 PyPI 仓库来升级，虽然第三方 PyPI 镜像下载会更快，但可能不是最新版本。

升级命令如下：

```bash
pip install --upgrade nvifan -i https://pypi.python.org/simple
```

如果你正在用 systemd 管理服务，升级后记得重启一下服务：

```bash
sudo systemctl restart nvifan
```

### 安装为服务（推荐）

想把这个工具设置为开机自启的服务吗？

很简单，运行以下命令即可：

```bash
sudo nvifan-install
```

### 卸载服务

想卸载这个服务吗？

输入以下命令即可：

```bash
sudo nvifan-uninstall
```

## 从源码安装

如果你想从源码安装这个工具，可以运行以下命令：

```bash
chmod +x install.sh
./install.sh
```

## 构建 Wheel

想构建这个工具的 Wheel 包吗？

运行以下命令就行了：

```bash
chmod +x build.sh
./build.sh
```

## 日志

这个工具的日志文件保存在 `/var/log/nvi/nvifan.log`。

如果你想查看日志，可以用以下命令：

```bash
sudo journalctl -u nvifan
```

或者

```bash
cat /var/log/nvi/nvifan.log
```

如果你在使用这个工具时遇到了问题，想要报告错误，记得附上日志文件。你可以在 GitHub 上创建一个 `Issue`，并把日志文件贴上去。

## Gitee

我们还有一个 Gitee 仓库，这个仓库是 GitHub 仓库的镜像，主要是为了方便国内用户下载。但请注意：

- **不要**在这个 Gitee 仓库上进行开发或提交 `Pull Request`。
- **不要**在 Gitee 上创建 `Issue`，因为我们不会查看 Gitee 上的 `Issue`。

## 参考

这个工具是基于
[CoolGPUs](https://github.com/andyljones/coolgpus)
和
[nvitop](https://github.com/XuehaiPan/nvitop)
开发的。
感谢他们的工作。
