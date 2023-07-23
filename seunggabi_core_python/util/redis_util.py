import redis

from seunggabi_core_python.exception.bad_request import BadRequest
from seunggabi_core_python.util import json_util

PORT = 6379
TTL = 10


def conn(
    host: str = None,
    port: int = PORT
):
    if host is None:
        raise BadRequest()

    return redis.Redis(
        host=host,
        port=port,
    )


def get(key: str = None):
    o = conn().get(key)
    if o:
        return json_util.to_dict(o)
    return o


def set(
    key: str = None,
    value=None,
    ttl: int = TTL,
):
    r = conn()

    r.set(key, json_util.pretty(value))
    r.expire(key, ttl)

    return value
