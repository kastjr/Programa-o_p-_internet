import requests
from bs4 import BeautifulSoup

# Solicita a URL da página do usuário
url = input("Digite a URL da página: ")

# Faz a solicitação HTTP da página e armazena o conteúdo HTML em uma variável
response = requests.get(url)
html_content = response.content

# Solicita a tag que o usuário deseja exibir
tag = input("Digite a tag que você deseja exibir: ")

# Analisa o HTML da página usando o BeautifulSoup e encontra todas as tags correspondentes
soup = BeautifulSoup(html_content, 'html.parser')
tags = soup.find_all(tag)

# Exibe o conteúdo de cada tag encontrada
for tag in tags:
    print(tag.text)
