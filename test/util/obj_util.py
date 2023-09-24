import pytest
from util.obj_util import *


def test_safe_get_key_exists():
    obj = {"a": 1, "z": {"b": 0}}
    result = safe_get(obj, "a")
    assert result == 1


def test_safe_get_key_not_exists():
    obj = {"a": 1, "z": {"b": 0}}
    result = safe_get(obj, "b")
    assert result is None


def test_safe_get_key_not_exists_with_default():
    obj = {"a": 1, "z": {"b": 0}}
    result = safe_get(obj, "b", 3)
    assert result == 3


def test_safe_get_nested_key():
    obj = {"a": 1, "z": {"b": 0}}
    result = safe_get(obj, "z.b")
    assert result == 0


def test_safe_get_numeric_key():
    obj = {"a": [10, 20, 30]}
    result = safe_get(obj, "a.1")
    assert result == 20


def test_safe_get_numeric_key_force_str():
    obj = {"a": [10, 20, 30]}
    result = safe_get(obj, "a.1", force_key_str=True)
    assert result is None


if __name__ == "__main__":
    pytest.main()
