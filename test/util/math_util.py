import pytest
from util.math_util import *


def test_safe_divide_nonzero_divisor():
    result = safe_divide(10, 2)
    assert result == 5.0


def test_safe_divide_zero_divisor():
    result = safe_divide(10, 0)
    assert result == 0


def test_safe_range_within_range():
    result = safe_range(5, 0, 10)
    assert result == 5


def test_safe_range_below_min():
    result = safe_range(-5, 0, 10)
    assert result == 0


def test_safe_range_above_max():
    result = safe_range(15, 0, 10)
    assert result == 10


if __name__ == "__main__":
    pytest.main()
