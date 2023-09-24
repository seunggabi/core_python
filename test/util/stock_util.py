import pytest
from util.stock_util import *


def test__unit():
    assert Decimal("0.001") == unit(0.1)
    assert Decimal("0.01") == unit(1)
    assert Decimal("0.1") == unit(10)
    assert Decimal("1") == unit(100)
    assert Decimal("5") == unit(1000)


def test__gap():
    assert 11 == gap(100, 110)


if __name__ == "__main__":
    pytest.main()
