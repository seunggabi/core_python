import pytest
from util.math_util import *


def test_safe_divide_nonzero_divisor():
    actual = safe_divide(10, 2)
    assert actual == 5.0


def test_safe_divide_zero_divisor():
    actual = safe_divide(10, 0)
    assert actual == 0


def test_safe_range_within_range():
    actual = safe_range(5, 0, 10)
    assert actual == 5


def test_safe_range_below_min():
    actual = safe_range(-5, 0, 10)
    assert actual == 0


def test_safe_range_above_max():
    actual = safe_range(15, 0, 10)
    assert actual == 10


if __name__ == "__main__":
    pytest.main()
