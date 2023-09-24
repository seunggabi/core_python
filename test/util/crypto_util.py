import pytest
from util.crypto_util import *


def test_md5():
    result = md5("hello", "world")
    expected = "063f9967ee3546c6f16fbd578e75a1c6"
    assert result == expected


def test_sha256():
    result = sha256("hello", "world")
    expected = (
        "a0f810d3ebed63263f4b4f5921fbab7799daa8f08134cb4844916b9e13cf3fc0"
    )
    assert result == expected


def test_encode():
    result = encode("hello world")
    expected = "aGVsbG8gd29ybGQ="
    assert result == expected


def test_decode():
    encoded_str = "aGVsbG8gd29ybGQ="
    expected = "hello world"

    result = decode(encoded_str)
    assert result == expected


def test_crypt():
    seed = "secret"
    result = crypt("password", seed)

    assert result


if __name__ == "__main__":
    pytest.main()
