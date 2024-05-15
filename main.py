import requests
from bs4 import BeautifulSoup

url = 'https://pypi.org/'

response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')

etiqueta_a = soup.find_all('a')
results = []

for a in etiqueta_a:
    results.append(a['href'])
print(results)

