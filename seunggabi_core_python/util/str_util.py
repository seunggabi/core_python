from typing import Union


def comma(n: Union[int, float]) -> str:
    return "{:,}".format(n)
