import requests
import sys
from bs4 import BeautifulSoup

url ='https://ligamx.net'
pagina = requests.get(url)
html = BeautifulSoup(pagina.content,'html.parser')
busqueda = html.find_all('a','tpts loadershow col-xs-9 hidden-xs')
equipo_lista = [team.text.strip() for team in busqueda]  #quitar espacios 
for index, team in enumerate(equipo_lista):
    print(f"{index + 1}.- {team}")
