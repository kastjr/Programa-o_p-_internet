import requests
from bs4 import BeautifulSoup

# URL da página a ser baixada
url = "https://www.starplus.com/pt-br"

# Termo a ser buscado na página
termo = "jogos"

response = requests.get(url)

# Extrai o texto da página sem as tags
soup = BeautifulSoup(response.content, "html.parser")
texto = soup.get_text()

# Exibe os 20 primeiros e os 20 últimos caracteres do texto
print("Primeiros 20 caracteres: ", texto[:20])
print("Últimos 20 caracteres: ", texto[-20:])

ocorre = []
posicao = -1
while True:
    posicao = texto.find(termo, posicao + 1)
    if posicao == -1:
        break
    ocorre.append(posicao)

print("Ocorrências encontradas:", ocorre)
