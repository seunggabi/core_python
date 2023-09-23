import pytest
from util import json_util
from util.file_util import *

PATH = os.path.dirname(os.path.dirname(__file__))


def test__read():
    assert read(f"{PATH}/requirements.txt") == "pytest\npytest-cov"


def test__read_all():
    expect = {"a.json": {"asdf": 1234}, "b.json": {"qwer": "asdf"}}
    for k, v in read_all(f"{PATH}/static/", ".json$").items():
        assert expect[k] == json_util.to_dict(v)


def test__name():
    assert ["a.json", "b.json"] == name(f"{PATH}/static/", ".json$")
    assert ["a.txt"] == name(f"{PATH}/static/", ".txt$")


if __name__ == "__main__":
    pytest.main()
