from typing import Union
from decimal import Decimal


def comma(n: Union[int, float, Decimal]) -> str:
    return "{:,}".format(n)
