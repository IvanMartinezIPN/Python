import re

# Regex1
nombre = r'Ivan'
cadena = 'Hola, mi nombre es Ivan y estoy practicando el uso de regex'
busqueda = re.findall(nombre, cadena, flags=re.I)
print(f'Salida: {busqueda}')

# Regex 2
regex = r'^[A-Z]{2}[1-9]{4}\-[a-z][0-9]$'
cadena = ['AB1234-f0', 'NK1501-a2','IB4567-k3','asda3453qw','AV1235af']
for prueba in cadena:
    if re.match(regex, prueba):
        print(f'Cadena {prueba}  valida')
    else: print(f'Cadena {prueba} invalida')

# Regex 3
regex3 = r'acero'
cadena = '''Entonces el desconocido saludó mientras el vivo acero se
enfriaba a altas temperaturas. Nuestro campeón recordó sus días
de herrero donde de igual forma trabajó con acero, no pudiendo
observar los errores del desconocido al trabajar con acero, pues
su acero era de mala calidad y para empeorar las cosas, dicho
acero estaba siendo mal enfriado y martillado. Cualquier maestro
herrero del acero hubiera quedado horrorizado al ver semejante
trato y calidad de dicho acero.
'''
print(f'Salida: {len(re.findall(regex3, cadena, flags=re.I))}')