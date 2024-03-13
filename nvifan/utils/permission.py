import os


def check_sudo():
    return os.geteuid() == 0


if __name__ == "__main__":
    print(check_sudo())
