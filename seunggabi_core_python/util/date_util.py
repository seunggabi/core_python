from datetime import datetime


def today(fmt: str = "%Y%m%d") -> str:
    return datetime.now().strftime(fmt)
