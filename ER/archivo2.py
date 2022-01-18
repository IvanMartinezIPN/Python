import re

lista=['Fabián Josafat Díaz Silleros',
'Miriam Paola Sosa Toledo',
'Emma Belem Andrade Hernández',
'Carlos Ignacio Rodríguez Granados',
'Maria del Sol Silva Hernández',
'Isla Griselda Ponce Mendoza',
'Christopher Agustin Maya Guardado',
'César Rodrigo Méndez Hernández',
'Edgar Alejandro Ramírez Fuentes',
'José Iván Martínez Alvarado',
'Alejandro González Torres',
'Diego Armando Vivanco Quintanar',
'Esteban Flores',
'María Antonieta3',
'Edgar Navarro2',
'Martin Navarro',
'Miriam Cabello',
'Sofia Granados',
'Mario Vallarta']

for name in lista:
    #print(name)

    if re.findall(r'(^M)',name):
        print(name)
    
    if re.findall(r'(s$)',name):
        print('1' + name)
    if re.findall(r'(Mari[oa])',name):
        print('2' + name)
    if re.findall(r'^([A-F])',name):
        print('3' + name)
    if re.findall(r'([a-z1-3]$)', name):
        print(name)

#^ inicio
#$ final
#[a-z] rango
