import requests

# Lê o CEP a ser pesquisado
cep = input("Digite o CEP: ")

# Faz a requisição à API da ViaCEP
url = f"https://viacep.com.br/ws/{cep}/json/"
response = requests.get(url)

# Verifica se a requisição foi bem sucedida
if response.status_code == 200:
    # Extrai os dados do endereço da resposta JSON
    dados_endereco = response.json()
    logradouro = dados_endereco["logradouro"]
    complemento = dados_endereco["complemento"]
    bairro = dados_endereco["bairro"]
    localidade = dados_endereco["localidade"]
    uf = dados_endereco["uf"]
    
    # Exibe o endereço completo
    endereco_completo = f"{logradouro}, {complemento} - {bairro}, {localidade}/{uf}"
    print("Endereço completo:", endereco_completo)
else:
    print("Erro ao buscar o endereço.")
