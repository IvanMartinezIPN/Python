import csv
lista_correos=[]

with open('datos1.csv',encoding='UTF8') as documento:
    #encoding para acentos
    lectura = csv.reader(documento)
    print(lectura)
    for i in lectura:
        correo=i[2]
        lista_correos.append(correo)
    print(lista_correos)
    #revisar listas comprimidas