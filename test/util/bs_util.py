import pytest
from unittest.mock import patch
from util.bs_util import crawl

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


if __name__ == "__main__":
    pytest.main()
