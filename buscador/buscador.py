import requests
from bs4 import BeautifulSoup

def search(keyword, url, depth):
    # Lista para armazenar as URLs a serem visitadas
    urls_to_visit = [url]

    # Dicionário para armazenar as ocorrências da palavra-chave
    keyword_occurrences = {}

    # Loop para visitar as páginas de acordo com a profundidade especificada
    for i in range(depth):
        # Lista para armazenar as novas URLs descobertas nesta iteração
        new_urls_to_visit = []

        # Loop para visitar cada URL na lista atual de URLs a visitar
        for url_to_visit in urls_to_visit:
            try:
                # Faz a solicitação HTTP da página e armazena o conteúdo HTML em uma variável
                response = requests.get(url_to_visit)
                html_content = response.content

                # Analisa o conteúdo HTML da página com a biblioteca Beautiful Soup
                soup = BeautifulSoup(html_content, 'html.parser')

                # Conta o número de ocorrências da palavra-chave na página e adiciona ao dicionário de ocorrências
                keyword_count = str(soup).count(keyword)
                if keyword_count > 0:
                    keyword_occurrences[url_to_visit] = keyword_count

                # Encontra todas as tags <a> na página e adiciona as URLs a serem visitadas à lista de novas URLs a visitar
                links = soup.find_all('a')
                for link in links:
                    new_url = link.get('href')
                    if new_url not in new_urls_to_visit and new_url not in urls_to_visit:
                        new_urls_to_visit.append(new_url)
            except:
                pass

        # Define a lista de URLs a visitar para a lista de novas URLs a visitar descobertas nesta iteração
        urls_to_visit = new_urls_to_visit

    # Ordena o dicionário de ocorrências por ordem decrescente de número de ocorrências
    keyword_occurrences = dict(sorted(keyword_occurrences.items(), key=lambda x: x[1], reverse=True))

    # Exibe as ocorrências da palavra-chave
    print(f"Ocorrências da palavra-chave '{keyword}':")
    for url, count in keyword_occurrences.items():
        print(f"{url}: {count}")
