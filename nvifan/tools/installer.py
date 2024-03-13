# -*- coding: utf-8 -*-

from nvifan.utils.command import do_command
from nvifan.utils.permission import check_sudo

service_target_path = "/etc/systemd/system/nvifan.service"
service_template = """
[Unit]
Description=NVIDIA GPU Fan Control on Linux
After=syslog.target

[Service]
ExecStart={}
Restart=on-failure
RestartSec=5s
ExecStop=/bin/kill -2 $MAINPID
KillMode=none

[Install]
WantedBy=multi-user.target
"""


def install():
    ret = do_command("which nvifan")
    if ret[0] != 0:
        print('"nvifan" is not available')
        exit(1)

    print("nvifan Path: " + ret[1])

    if not check_sudo():
        print('Please use "sudo nvifan-installer"')
        exit(-1)

    final_text = service_template.format(ret[1]).strip() + "\n"

    # Write To Service
    try:
        with open(service_target_path, "w", encoding="utf-8") as f:
            f.write(final_text)
        print("Service Configure Path:\n" + service_target_path)
        print("Successfully installed service.")
    except Exception as e:
        print("Failed to write to service file")
        e_str: str = str(e)
        print(e_str)
        if e_str.find("Permission denied") != -1:
            print('Please use "sudo nvifan-installer"')
        exit(-1)


def uninstall():
    if not check_sudo():
        print('Please use "sudo nvifan-uninstall"')
        exit(-1)

    try:
        # Delete Service File
        do_command("systemctl stop nvifan")
        do_command("systemctl disable nvifan")
        do_command("rm -f " + service_target_path)
    except Exception as e:
        print("Failed to delete service file!")
        e_str: str = str(e)
        print(e_str)
        if e_str.find("Permission denied") != -1:
            print('Please use "sudo nvifan-uninstall"')
        exit(-1)


if __name__ == "__main__":
    install()
    uninstall()
