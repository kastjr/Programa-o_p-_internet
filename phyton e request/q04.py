import requests

# URL da imagem a ser baixada
url = "https://www.google.com/url?sa=i&url=https%3A%2F%2Fturbologo.com%2Fpt%2Fblog%2Fpremier-league-logo%2F&psig=AOvVaw2yo-CVFkM31p55r5ELowpr&ust=1677757853899000&source=images&cd=vfe&ved=0CBEQjhxqFwoTCMCSgYrVuv0CFQAAAAAdAAAAABAE"

# Nome do arquivo local a ser salvo
nome_arquivo = "imagem.jpg"

# Faz o download da imagem
response = requests.get(url)

# Salva a imagem localmente
with open(nome_arquivo, "exemplo") as arquivo:
    arquivo.write(response.content)
