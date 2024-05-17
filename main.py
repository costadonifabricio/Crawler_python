import requests
from bs4 import BeautifulSoup
import json

url = 'https://pypi.org/'

response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')

etiqueta_a = soup.find_all('a')
results = []

for a in etiqueta_a:
    results.append(a['href'])

data = {}

for enlace in results:
    try:
        if enlace.startswith('http'):
            respuesta = requests.get(enlace)
            sopita = BeautifulSoup(respuesta.text, 'html.parser')
            h1_etiqueta = [str(h1) for h1 in sopita.find_all('h1')]
            p_etiqueta = [str(p) for p in sopita.find_all('p')]
            data[enlace] = h1_etiqueta + p_etiqueta
    except Exception as e:
        print(f"Error al procesar el enlace {enlace}: {e}")

with open('data.json', 'w') as f:
    json.dump(data, f, indent=4, sort_keys=True)