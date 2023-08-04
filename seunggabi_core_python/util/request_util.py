import requests

from typing import Union
from seunggabi_core_python.exception.not_ok import NotOk


def get(
    url: str,
    params: Union[dict, None] = None,
    retry: int = 3,
) -> dict:
    params = params or {}

    response = requests.get(url, params=params)
    if response.status_code == 200:
        try:
            return response.json()
        except:
            return response.text
    else:
        retry -= 1
        if retry == 0:
            raise NotOk(response.text)

        return get(url, params, retry)
