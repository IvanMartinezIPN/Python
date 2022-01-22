import csv

with open('archivoTA.csv',encoding='UTF8') as documento:
    #encoding para acentos
    lectura = csv.reader(documento)
    print(lectura)
    for i in lectura:
        print(i)
