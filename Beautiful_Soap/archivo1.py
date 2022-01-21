from urllib import request
import requests
from bs4 import BeautifulSoup

page = requests.get('http://protecounam.mx/home',timeout=1)

variable_parseo = BeautifulSoup(page.text,'html.parser')
print(variable_parseo)
info = variable_parseo.find_all('li')
print(info)

for i in info:
    print(i)
    #print(i.text)
    sub = i.find_all('a')
    print(sub)
    print(sub[0].attrs.get('href'))

url = 'https://ww.eldolar.info/es-MX/mexico/dia/hoy'
page = requests.get(url,timeout = 1)
variable_parseo = BeautifulSoup(page.content, 'html.parser')
busqueda = variable_parseo.find_all('span','xTimes')
print(busqueda)

valor = busqueda[1].text
print(valor)


url = 'https://ligamx.net'

acceso_page = requests.get(url)
var_parseo = BeautifulSoup(acceso_page.content,'html.parser_class')
busqueda = var_parseo.find_all('a','tpst loadershow col-xs-9 hidden-xs')

#print(busqueda)

lista_equipo=[]

for i in lista_equipo:
    print(i.text)
    lista_equipo.append(i.text)

print(lista_equipo)