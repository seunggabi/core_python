import pytest
from util.date_util import *
from datetime import datetime


def test_today_default_format():
    expected_format = "%Y%m%d"
    result = today()
    current_datetime = datetime.now()
    expected = current_datetime.strftime(expected_format)
    assert result == expected


def test_today_custom_format():
    custom_format = "%Y-%m-%d"
    result = today(fmt=custom_format)
    current_datetime = datetime.now()
    expected = current_datetime.strftime(custom_format)
    assert result == expected


def test_isoformat():
    expected = datetime.now().isoformat().split(".")[0]
    result = isoformat().split(".")[0]
    assert result == expected


def test_timestamp():
    expected = int(float(time.time()))
    result = int(float(timestamp()))
    assert result == expected


if __name__ == "__main__":
    pytest.main()
