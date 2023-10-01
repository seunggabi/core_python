import pytest
from unittest.mock import patch
from util.bs_util import crawl, soup

SAMPLE_HTML_CONTENT = """
<html>
  <body>
    <div>
      <a href="/ko/charts/#dominance-percentage">Sample Text</a>
    </div>
  </body>
</html>
"""

URL = "https://coinmarketcap.com/ko/charts/"
OBJ = {"href": "/ko/charts/#dominance-percentage"}


@patch(
    "seunggabi_core_python.util.request_util.get",
    return_value=SAMPLE_HTML_CONTENT,
)
def test_crawl(mock_get):
    result = crawl(url=URL, obj=OBJ)
    expected = "Sample Text"
    assert result == expected


@patch(
    "seunggabi_core_python.util.request_util.get",
    return_value=SAMPLE_HTML_CONTENT,
)
def test_soup(mock_get):
    result = soup(url=URL, obj=OBJ)
    expected = "Sample Text"
    assert result.get_text() == expected


if __name__ == "__main__":
    pytest.main()
