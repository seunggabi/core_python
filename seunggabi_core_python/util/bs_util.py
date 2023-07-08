from seunggabi_core_python.util import request_util
from bs4 import BeautifulSoup


def crawl(
    url: str = None,
    obj: dict = None,
    index: int = 0
):
    contents = request_util.get(url)
    soup = BeautifulSoup(contents, "html.parser")

    return soup.findAll(**obj)[index].get_text()


if __name__ == '__main__':
    url = "https://coinmarketcap.com/ko/charts/"
    obj = {"href": "/ko/charts/#dominance-percentage"}

    print(crawl(url, obj))
