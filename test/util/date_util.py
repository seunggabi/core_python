import pytest
from util.date_util import *
from datetime import datetime


# 테스트 케이스: today 함수 테스트
def test_today_default_format():
    expected_format = "%Y%m%d"
    actual = today()
    current_datetime = datetime.now()
    expected = current_datetime.strftime(expected_format)
    assert actual == expected


def test_today_custom_format():
    custom_format = "%Y-%m-%d"
    actual = today(fmt=custom_format)
    current_datetime = datetime.now()
    expected = current_datetime.strftime(custom_format)
    assert actual == expected


def test_isoformat():
    expected = datetime.now().isoformat().split(".")[0]
    actual = isoformat().split(".")[0]
    assert actual == expected


def test_timestamp():
    expected = int(float(time.time()))
    actual = int(float(timestamp()))
    assert actual == expected


if __name__ == "__main__":
    pytest.main()
