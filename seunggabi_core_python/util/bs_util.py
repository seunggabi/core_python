from seunggabi_core_python.util import request_util
from bs4 import BeautifulSoup


def crawl(url: str = None, obj: dict = None, index: int = 0):
    contents = request_util.get(url)
    soup = BeautifulSoup(contents, "html.parser")

    return soup.findAll(**obj)[index].get_text()
