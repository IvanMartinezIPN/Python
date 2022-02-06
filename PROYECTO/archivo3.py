import requests
import sys
import re
from bs4 import BeautifulSoup

url = 'https://www.kavak.com/comprar-Chevrolet/tipo-hatchback/precio-93182-min/compra-de-autos'
pagina = requests.get(url)
html = BeautifulSoup(pagina.content,'html.parser')
carro = html.find_all('div', 'card-body')
print("A continuacion te mostramos algunas recomenaciones:\n")
for mostrar in carro:
    nombre = mostrar.find('h2', 'car-name').text.strip()
    año = int(mostrar.find('p', 'car-details').text.strip().split(' ')[0])
    precio = float(re.sub(',', '.', mostrar.find('span', 'payment-highlight payment-total').text.strip()[1:]))
    no = re.compile('Sonic', flags=re.I)
    sonic = no.search(nombre)
    if not sonic and precio < 220_000 and año > 2017:
        print('***********************************************************')
        print(f'\tNombre: { nombre }')
        print(f'\tAño: {año}')
        print(f'\tPrecio: {precio}')
        print('***********************************************************')