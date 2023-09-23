import pytest
from util.str_util import *


def test__comma():
    assert "1,123,000" == comma(1123000)
    assert "3,000" == comma(3000)
    assert "3,000.123" == comma(3000.123)
    assert "123" == comma(Decimal(123))


if __name__ == "__main__":
    pytest.main()
