import re
nick_names = ["navegante",
"Navegante",
"NaVeGaNtE",
"NAVEGANTE88",
"un_navegante",
"NaveGANTE_02"]

for nickname in nick_names:
    if re.search('^navegante([0-9]*)',nickname, flags = re.I) is not None: print(nickname)
#re.I busqueda sin distincion en mayuscula y minuscula

#EJERCICIO DE CURP
curp = input('Ingresa el CURP: ')

if re.search(r'(^[A-Z]{4}[0-9]{6}[M|H][A-Z]{5}([A-Z]|[0-9][0-9]))',curp):
    print('Curp ' + curp + ' valido')
else:
    print('Curp invalido')

#EJERCICO CON FECHA DD/MM/AAAA

usuario = input('Dame la fecha con ormato DD/MM/AAAA')

if re.search(r'((0[1-9]|3[0-1]|[1-2][0-9])\/(0[1-9]|1[0-2])\/[0-9]{4})',usuario) is not None:
    print('Formato valido')
else: 
    print('Formato invalido')

#EJERCICIO DE CORREO
lista_correos = ["correo1_abcd@hotmail.com",
"hola23.gmail.com",
"adc071@gmail.com",
"cesar123123@yahogmail.com",
"favs002@yahoo.com",
"alex cerro123@outlook.mx",
"javier@ciencias.unam.mx",
"andrea123.flores@comunidad.unam.mx",
"123raul@yahoo.mx",
"bruno099 live.es"]

for correo in lista_correos:
    if re.search(r'(^[A-Z0-9]+[^\s]+\@gmail.com)',correo, flags = re.I) is not None:
        print(correo)