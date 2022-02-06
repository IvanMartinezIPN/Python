import json
from types import MemberDescriptorType


with open('segundoarchivocls.json','r') as archivo:
    info = json.load(archivo)
    members = info['members']
    members = {member['name'] : member['powers'] for member in members }
    print("Powers list :")
    for name, powers in members.items():
        print(f'\n{name} superpowers:') #Bandera para poder imprimir el nombre del heroe 
        for power in powers:
            print(power)