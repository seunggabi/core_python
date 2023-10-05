import requests

from typing import Union, Any
from seunggabi_core_python.exception.not_ok import NotOk

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
}

OK = 200
RETRY = 3


def ok(response):
    try:
        return response.json()
    except:
        return response.text


def get(
    url: str,
    params: Union[dict, None] = None,
    retry: int = RETRY,
    headers=None,
) -> Any:
    params = params or {}
    headers = headers or HEADERS

    response = requests.get(
        url,
        params=params,
        headers=headers,
    )

    if response.status_code == OK:
        return ok(response)

    retry -= 1
    if retry <= 0:
        raise NotOk(response.text)

    return get(url, params, retry, headers)


def post_data(
    url: str,
    data: Union[dict, None] = None,
    retry: int = RETRY,
    headers=None,
) -> Any:
    data = data or {}
    headers = headers or HEADERS

    response = requests.post(
        url,
        data=data,
        headers=headers,
    )

    if response.status_code == OK:
        return ok(response)

    retry -= 1
    if retry <= 0:
        raise NotOk(response.text)

    return post_data(url, data, retry, headers)


def post_json(
    url: str,
    json: Union[dict, None] = None,
    retry: int = RETRY,
    headers=None,
) -> Any:
    json = json or {}
    headers = headers or HEADERS

    response = requests.post(
        url,
        json=json,
        headers=headers,
    )

    if response.status_code == OK:
        return ok(response)

    retry -= 1
    if retry <= 0:
        raise NotOk(response.text)

    return post_json(url, json, retry, headers)
