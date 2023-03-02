import requests
from bs4 import BeautifulSoup
import re
from urllib.parse import urljoin


class Page:
    def __init__(self, url: str,):
        self.url = url
        self.links = []
        self.foudedTerms = []
        self.pointedBy = []


visitedPages = {}


def find(url: str, query: str, depth: int):

    response = requests.get(url, ferify=False)

    soup = BeautifulSoup(response.content, 'html.parser')

    text = soup.get_text()

    regex = re.compile(r"([^\.]{0,50}" + query + r".{0,50})")
    resultList = regex.findall(text)

    links = []

    for tag in soup.find_all("a"):
        link = tag.get("href")

        links.append(link)

        page = Page(url)
        page.links = links
        page.foundedTerms = resultList

        visitedPages[url] = page

        for link in page.links:
            if link in visitedPages:
                visitedPages[link].pointedBy.append(page)

    if (depth > 0):
        for link in links:
            find(link, query, depth - 1)

    print("")
