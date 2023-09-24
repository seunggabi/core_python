import redis

from seunggabi_core_python.exception.bad_request import BadRequest
from seunggabi_core_python.util import json_util

PORT = 6379
TTL = 10


def conn(
    host: str = None,
    port: int = PORT,
):
    if host is None:
        raise BadRequest()

    return redis.Redis(
        host=host,
        port=port,
    )


def get(
    conn=None,
    key: str = None,
):
    if conn is None:
        raise BadRequest()

    o = conn.get(key)
    if not o:
        return None

    try:
        return json_util.to_dict(o)
    except:
        return o.decode()


def set(
    conn=None,
    key: str = None,
    value=None,
    ttl: int = TTL,
):
    if conn is None:
        raise BadRequest()

    conn.set(key, json_util.pretty(value))
    conn.expire(key, ttl)

    return value
