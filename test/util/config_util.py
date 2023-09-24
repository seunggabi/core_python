import pytest
from unittest.mock import patch, mock_open
from util.config_util import *

GROUP = "upbit"
CONTEXT = "credentials"


def test_get_valid():
    config_content = """
    [DEFAULT]
    key = default_key
    secret = default_secret

    [test_profile]
    key = test_key
    secret = test_secret
    """

    with patch("builtins.open", mock_open(read_data=config_content)):
        result = get(group=GROUP, context=CONTEXT, profile="test_profile")

    expected = {"key": "test_key", "secret": "test_secret"}
    assert result == expected


def test_get_missing_group_context():
    with pytest.raises(BadRequest):
        get(group=None, context=None, profile="test_profile")


def test_get_file_not_found():
    with pytest.raises(NotFound):
        get(
            group="nonexistent_group",
            context="nonexistent_context",
            profile="test_profile",
        )


if __name__ == "__main__":
    pytest.main()
