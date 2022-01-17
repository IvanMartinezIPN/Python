import json
with open('segundoarchivocls.json','r') as archivo:
    info = json.load(archivo)
    print(info)

with open('segundoarchivocls.json','r') as archivo:
    info = json.load(archivo)
    print(info['members'][0]['name'])
    