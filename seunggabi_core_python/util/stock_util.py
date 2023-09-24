from typing import Union
from decimal import Decimal


def unit(n: Union[int, float, Decimal]):
    n = abs(n)
    index = str(n).find(".")

    if n < 1:
        pow = len(str(n)[index + 1 :])

        v = Decimal("0.01")
        for _ in range(pow):
            v /= Decimal(10)

        return v

    if n < 10:
        return Decimal("0.01")
    if n < 100:
        return Decimal("0.1")

    n = int(n)
    m = len(str(n))

    v = 10 ** ((m - 3) // 2)
    if m % 2 == 0:
        v *= 5

    return int(v)


def gap(
    start: Union[int, float, Decimal], end: Union[int, float, Decimal]
) -> int:
    cnt = 0
    while start <= end:
        start += unit(start)
        cnt += 1

    return cnt
