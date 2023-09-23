import pytest
from util.json_util import *


def test_to_dict_valid_json():
    json_str = '{"name": "John", "age": 30, "city": "New York"}'
    result = to_dict(json_str)
    expected = {"name": "John", "age": 30, "city": "New York"}
    assert result == expected


def test_pretty_dict():
    input_dict = {"name": "John", "age": 30, "city": "New York"}
    result = pretty(input_dict)
    expected = (
        '{\n    "age": 30,\n    "city": "New York",\n    "name": "John"\n}'
    )
    assert result == expected


def test_pretty_json_str():
    json_str = '{"name": "John", "age": 30, "city": "New York"}'
    result = pretty(json_str)
    expected = (
        '{\n    "age": 30,\n    "city": "New York",\n    "name": "John"\n}'
    )
    assert result == expected


def test_pretty_invalid_input():
    invalid_input = "This is not JSON"
    result = pretty(invalid_input)
    assert result == invalid_input


if __name__ == "__main__":
    pytest.main()
