import requests
import re

# Solicita a URL da página do usuário
url = input("Digite a URL da página: ")

# Faz a solicitação HTTP da página e armazena o conteúdo HTML em uma variável
response = requests.get(url)
html_content = response.content.decode('utf-8')

# Solicita o termo que o usuário deseja buscar
termo = input("Digite o termo que você deseja buscar: ")

# Procura o termo no conteúdo HTML usando a biblioteca re
ocorrencias = re.findall(termo, html_content)

# Exibe as ocorrências encontradas
if ocorrencias:
    print(f"O termo '{termo}' foi encontrado {len(ocorrencias)} vezes na página:")
    for ocorrencia in ocorrencias:
        print(ocorrencia)
else:
    print(f"O termo '{termo}' não foi encontrado na página.")
