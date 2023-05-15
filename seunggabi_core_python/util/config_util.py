import os
from configparser import ConfigParser

from seunggabi_core_python.const import DEFAULT, CREDENTIALS
from seunggabi_core_python.exception.bad_request import BadRequest


def home():
    return os.path.expanduser("~")


def path(
    group: str = None,
    context: str = None,
):
    return f".{group}/{context}"


def get(
    group: str = None,
    context: str = None,
    profile: str = None,
) -> dict:
    if group is None or context is None:
        raise BadRequest()

    profile = profile or DEFAULT

    config = ConfigParser()
    config.read(f"{home()}/{path(group, context)}")

    return config._sections[profile]


if __name__ == '__main__':
    print(
        get(
            group="upbit",
            context=CREDENTIALS,
        )
    )
