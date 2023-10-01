from seunggabi_core_python.util import request_util
from bs4 import BeautifulSoup


def soup(url: str = None, obj: dict = None, index: int = 0):
    return BeautifulSoup(request_util.get(url), "html.parser").findAll(**obj)[
        index
    ]


def crawl(url: str = None, obj: dict = None, index: int = 0):
    return soup(url, obj, index).get_text()
