import requests

termo = input("Digite o termo que você deseja buscar no Google: ")

url = f"https://www.google.com/search?q={termo}"
#simular um navegador
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"}

response = requests.get(url, headers=headers)
html_content = response.content.decode('utf-8')

print(html_content)
