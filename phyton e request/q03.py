import requests
import re
from bs4 import BeautifulSoup

# Solicita a URL da página do usuário
url = input("Digite a URL da página: ")

response = requests.get(url)

# Solicita o termo que o usuário deseja buscar
termo = input("Digite o termo que você deseja buscar: ")

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
    else:
        print(f"O termo '{termo}' não foi encontrado na página.")

