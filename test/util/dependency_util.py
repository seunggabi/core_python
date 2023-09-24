import pytest
import os

from util.dependency_util import *
from util.file_util import read

PATH = os.path.dirname(os.path.dirname(__file__))


def test_get():
    assert get() == read(f"{PATH}/../requirements.txt").split("\n")


if __name__ == "__main__":
    pytest.main()
