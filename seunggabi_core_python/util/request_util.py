import requests

from typing import Union


def get(
    url: str,
    params: Union[dict, None] = None
) -> dict:
    params = params or {}

    response = requests.get(url, params=params)
    try:
        return response.json()
    except:
        return response.text
