from util.env_util import *


def test_get_existing_env_variable():
    os.environ["TEST_KEY"] = "test_value"

    key = "TEST_KEY"
    result = get(key)

    assert result == "test_value"


def test_get_nonexistent_env_variable():
    if "TEST_KEY" in os.environ:
        del os.environ["TEST_KEY"]

    key = "NONEXISTENT_KEY"
    result = get(key)

    assert result is None
