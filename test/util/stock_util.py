import pytest
from util.stock_util import *


def test__unit():
    assert Decimal("0.01") == unit(1)


def test__gap():
    assert 11 == gap(100, 110)


if __name__ == "__main__":
    pytest.main()
