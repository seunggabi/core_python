from util import str_util


def test__comma():
    assert "1,123,000" == str_util.comma(1123000)
    assert "3,000" == str_util.comma(3000)
    assert "3,000.123" == str_util.comma(3000.123)
