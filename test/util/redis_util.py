import pytest
from mockredis import MockRedis
from util.redis_util import *


@pytest.fixture
def mock_redis_conn():
    return MockRedis()


def test_set_get_with_mock_redis(mock_redis_conn):
    key = "test_key"
    value = "test_value"

    set_result = set(mock_redis_conn, key, value)
    assert set_result == value

    get_result = get(mock_redis_conn, key)
    assert get_result == value


def test_get_nonexistent_key_with_mock_redis(mock_redis_conn):
    key = "nonexistent_key"

    get_result = get(mock_redis_conn, key)
    assert get_result is None


def test_conn():
    assert conn(host="host") is not None


def test_none_conn():
    with pytest.raises(BadRequest):
        set(conn=None, key="test_key", value="test_value")
    with pytest.raises(BadRequest):
        get(conn=None, key="test_key")
    with pytest.raises(BadRequest):
        conn(host=None)


if __name__ == "__main__":
    pytest.main()
