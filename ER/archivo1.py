import re

ch = 'My friend Edgar is argentine, he could been giving us classes but is a little lazy to do it'
print(re.search(r'friend',ch))

if re.search(r'Edgar',ch) is not None:
    print('Match')
else:
    print('No exist') 

searching = re.search(r'is',ch)
print(searching)
print(searching.start())
print(searching.end())
print(searching.span())

textse = 'lazy'

print(re.findall(textse,ch))  #retorna lista
print(len(re.findall(textse,ch)))



#search regresa el primer elemento de match y findall retrona una lista de matches