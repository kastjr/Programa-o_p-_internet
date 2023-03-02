import re
import requests
import requests_cache
from bs4 import BeautifulSoup
from requests.exceptions import InvalidSchema
from urllib.parse import urljoin

requests_cache.install_cache("cache")


class Page:
    def __init__(self, url: str):
        self.url = url
        self.title = ""
        self.links = []
        self.foundedTerms = []

# key: value
# url: Page
visitedPages = {}
referenceCount = {}


def find(url: str, depth: int):
    print(f"{depth} Acessando {url}...")
    try:
        response = requests.get(url)
    except InvalidSchema as e:
        return

    soup = BeautifulSoup(response.content, 'html.parser')

    text = soup.get_text()

    regex = re.compile(r"([^\.]{0,50}" + query + r".{0,50})")

    resultList = regex.findall(text)

    links = []
    for tag in soup.find_all("a"):
        link = tag.get("href")

        if link == None or len(link) == 0:
            continue
        try:
            links.append(urljoin(url, link))
        except:
            continue

    currentPage = Page(url)
    currentPage.title = soup.title.text if soup.title != None else "Sem titulo"
    currentPage.foundedTerms = resultList
    currentPage.links = links

    if url not in visitedPages:
        visitedPages[url] = currentPage

    for link in currentPage.links:
        if link in referenceCount:
            referenceCount[link] += 1
        else:
            referenceCount[link] = 1

        if depth > 0:
            if link not in visitedPages:
                find(link, depth - 1)

query = "abril"
find('https://pt.wikipedia.org/wiki/Campeonato_Mundial_de_H%C3%B3quei_no_Gelo_de_1982', 0)

visitedPagesList = [v for k, v in visitedPages.items()]
visitedPagesList = sorted(
    visitedPagesList,
    key=lambda x: len(x.foundedTerms),
    reverse=True
)
visitedPagesList = list(
    filter(lambda x: len(x.foundedTerms) > 0, visitedPagesList)
)

for page in visitedPagesList:
    print()
    print(page.url)
    print(page.title)
    print(page.foundedTerms[0])
    #print(f"Referencias a página: {referenceCount.__init__[Page]}")
