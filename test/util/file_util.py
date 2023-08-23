import os
from util import file_util, json_util

PATH = os.path.dirname(os.path.dirname(__file__))


def test__read():
    assert file_util.read(f"{PATH}/requirements.txt") == "pytest"


def test__read_all():
    expect = {
        "a.json": {
            "asdf": 1234
        },
        "b.json": {
            "qwer": "asdf"
        }
    }
    for k, v in file_util.read_all(f"{PATH}/static/", ".json$").items():
        assert expect[k] == json_util.to_dict(v)


def test__name():
    assert ["a.json", "b.json"] == file_util.name(f"{PATH}/static/", ".json$")
    assert ["a.txt"] == file_util.name(f"{PATH}/static/", ".txt$")
