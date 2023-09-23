import pytest
from requests_mock import Mocker
from util.request_util import *


@pytest.fixture
def mock_requests():
    with Mocker() as m:
        yield m


def test_successful_get_request(mock_requests):
    url = "https://example.com/api/data"
    response_data = {"key": "value"}

    mock_requests.get(url, json=response_data, status_code=200)

    actual = get(url)

    assert actual == response_data


def test_failed_get_request_with_retry(mock_requests):
    url = "https://example.com/api/data"
    error_message = "Something went wrong"

    for _ in range(3):
        mock_requests.get(url, text=error_message, status_code=500)

    with pytest.raises(NotOk) as exc_info:
        get(url)

    assert str(exc_info.value) == str(NotOk(error_message))


def test_failed_get_request_without_retry(mock_requests):
    url = "https://example.com/api/data"
    error_message = "Something went wrong"

    mock_requests.get(url, text=error_message, status_code=500)

    with pytest.raises(NotOk) as exc_info:
        get(url, retry=0)

    assert str(exc_info.value) == str(NotOk(error_message))


if __name__ == "__main__":
    pytest.main()
