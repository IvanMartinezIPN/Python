import json 
#Python a JSON
#dump en plural trabaja en el script en singular en el fichero

entero = 33
json_entero=json.dumps(entero) #transforma datos utilizando dump
print(json_entero)
print(type(json_entero))

#JSON a Python

python_entero=json.loads(json_entero)
print(python_entero)
print(type(python_entero))

Lista = ['Rompecabezas',(1,2,3,4),[.23,33,.23]]
#Python a JSON
json_lista = json.dumps(Lista)
print(json_lista)
print(type(json_lista))
print(type(Lista))
#JSON a Python
python_lista = json.loads(json_lista)
print(python_lista)
print(type(python_lista))

with open('json_creado.json','w') as archivo:
    json.dump(Lista,archivo)