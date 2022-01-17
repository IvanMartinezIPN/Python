import csv

with open('datos1.csv',encoding='UTF8') as documento:
    #encoding para acentos
    lectura = csv.reader(documento)
    print(lectura)
    for i in lectura:
        print(i)
        print(i[2])
