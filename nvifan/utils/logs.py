# -*- coding: utf-8 -*-

import os
import loguru

log_dir = "/var/log/nvi"

# Check Log Directory
if not os.path.exists("/var/log/nvi"):
    os.mkdir("/var/log/nvi")

log_path = os.path.join(log_dir, "nvifan.log")

logger = loguru.logger

logger.add(log_path, retention="30 days")


def get_logger() -> loguru.logger:
    return logger
