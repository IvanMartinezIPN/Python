from threading import Thread
#Funcion a ejecutar
def cuenta(n):
    contador = n
    while contador<10:
        print('')
        print(contador)
        contador +=1

#Creamos tareas a ejecutar en paralelo

h1 = Thread(target = cuenta, args =(1, ))
h2 = Thread(target = cuenta, args =(2, ))
h3 = Thread(target= cuenta, args =(3, ))
#Iniciamos las tareas

h1.start()
h2.start()
h3.start()
