import os
from configparser import ConfigParser

from const import DEFAULT, CREDENTIALS
from exception.bad_request import BadRequest
from exception.not_found import NotFound


def home() -> str:
    return os.path.expanduser("~")


def path(
    group: str = None,
    context: str = None,
) -> str:
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
    p = f"{home()}/{path(group, context)}"

    if not config.read(p):
        raise NotFound(p) from None

    return config._sections[profile]
