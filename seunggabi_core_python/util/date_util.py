import time
from datetime import datetime, timezone


def today(fmt: str = "%Y%m%d") -> str:
    return datetime.now().strftime(fmt)


def isoformat() -> str:
    return datetime.now().isoformat()


def timestamp() -> str:
    return str(time.time())


def ts(date: str, fmt: str = "%Y%m%d"):
    return int(datetime.strptime(date, fmt).timestamp())
