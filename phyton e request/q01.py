from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import re

requisicao = Request("https://www.starplus.com/pt-br")
html_ = urlopen(requisicao)

soup = BeautifulSoup(html_,"lxml")

for link in soup.findAll('a'):
    lis = link.get('href')
    if(not lis.find('https')):
        print(lis)
    
    
