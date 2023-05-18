import requests

from typing import Union


def get(
    url: str,
    params: Union[dict, None] = None
) -> dict:
    params = params or {}

    return requests.get(url, params=params).json()
