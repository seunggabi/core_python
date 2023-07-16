import os

from typing import Union


def get(key: str) -> Union[str, None]:
    o = os.environ

    return o[key] if key in o else None
