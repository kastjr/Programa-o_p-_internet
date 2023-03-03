import re
import requests
import requests_cache
from bs4 import BeautifulSoup
from requests.exceptions import InvalidSchema
from urllib.parse import urljoin

requests_cache.install_cache("cache")  # melhorar o desempenho da execução

# bibliotecas que guardam as paginas visitadas e a quantidade de referencias as páginas
visitedPages = {}
referenceCount = {}


class Page:
    def __init__(self, url: str):
        self.url = url
        self.title = ""
        self.links = []
        self.foundedTerms = []

# key: value
# url: Page

# Função principal


def find(url: str, term: str, depth: int):
    print(f"Profundidade {depth} Acessando {url}...")

    try:
        response = requests.get(url)
    except requests.exceptions.MissingSchema:
        return
    except requests.exceptions.InvalidSchema:
        return

# Faz o download da pagina e procura as referencias e contextos
    soup = BeautifulSoup(response.content, 'html.parser')
    text = soup.get_text()
    regex = re.compile(r"([^\.]{0,50}" + term + r".{0,50})")
    resultList = regex.findall(text)

    links = []

    for tag in soup.find_all("a"):
        if tag.get("href") != None:
            if tag.get("href").startswith('/'):
                link = "https://www.bbc.com" + tag.get("href")
            elif tag.get("href").startswith('http'):
                link = tag.get("href")
            else:
                link = None
                continue

            if link == None or len(link) == 0:
                continue
            else:
                try:
                    if link not in links:  # ignorando repetições
                        links.append(link)
                except:
                    continue

# Mostra o conteudo da pagina e se nela há referencias e seu determinado contexto
    currentPage = Page(url)
    currentPage.title = soup.title.text if soup.title != None else "Sem titulo"
    if len(resultList) != 0:
        currentPage.foundedTerms = resultList
    else:
        currentPage.foundedTerms = ['Não foi encontradas referências']
    currentPage.links = links

# Verifica se a pagina já foi visitada e adiona referencias a ela
    if url not in visitedPages:
        visitedPages[url] = currentPage
        referenceCount[url] = 1
    else:
        referenceCount[url] += 1

    if depth > 0:
        for link in currentPage.links:
            if link not in visitedPages:
                find(link, term, depth - 1)


term = "Ucrânia"
find('https://www.bbc.com/portuguese', term, 1)


for page in visitedPages.values():
    print()
    print(page.url)
    print(page.title)

    for n in range(len(page.foundedTerms)):

        print(n, "-", page.foundedTerms[n] + "\n")


print('fim')
