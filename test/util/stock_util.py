from util import stock_util
from decimal import Decimal


def test__unit():
    assert Decimal("0.01") == stock_util.unit(1)


def test__gap():
    assert 11 == stock_util.gap(100, 110)
