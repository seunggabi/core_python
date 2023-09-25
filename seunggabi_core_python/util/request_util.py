import requests

from typing import Union, Any
from seunggabi_core_python.exception.not_ok import NotOk


def get(
    url: str,
    params: Union[dict, None] = None,
    retry: int = 3,
    headers=None,
) -> Any:
    params = params or {}
    headers = headers or {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
    }

    response = requests.get(
        url,
        params=params,
        headers=headers,
    )

    if response.status_code == 200:
        try:
            return response.json()
        except:
            return response.text
    else:
        retry -= 1
        if retry <= 0:
            raise NotOk(response.text)

        return get(url, params, retry)
