# -*- coding: utf-8 -*-

import subprocess
from typing import Tuple


def do_command(cmd: str) -> Tuple[int, str]:
    """
    执行命令行，返回执行状态和输出信息。

    参数:
    cmd (str): 要执行的命令行。

    返回:
    Tuple[int, str]: 一个元组，包含执行状态码和输出信息。
    如果执行成功，状态码为0；否则为其他值。
    """
    try:
        # 执行命令行，并捕获输出和错误输出
        process = subprocess.run(
            cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True
        )
        output = process.stdout + process.stderr  # 合并标准输出和错误输出
        return_code = process.returncode
    except subprocess.CalledProcessError as e:
        # 如果发生异常（例如，命令不存在），返回执行状态和异常信息
        return_code = e.returncode
        output = e.output
    except Exception as e:
        # 处理其他可能发生的异常
        return_code = 1
        output = str(e)

    return return_code, output
