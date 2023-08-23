import os
from util import file_util

PATH = os.path.dirname(os.path.dirname(__file__))


def test_read():
    assert file_util.read(f"{PATH}/requirements.txt") == "pytest"


def test_count():
    assert file_util.count(f"{PATH}/static/", ".json$") == 2
    assert file_util.count(f"{PATH}/static/", ".txt$") == 1
