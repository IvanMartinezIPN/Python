from threading import Thread
import time

def hilo1():
    print('\nEmpieza hilo 1')
    time.sleep(10)
    print('\nHilo 1 termina')


def hilo2():
    print('\nEmpieza hilo 2')
    time.sleep(4)
    print('\nHilo 2 termina')   

print('Inicai el programa principal')
#Creamos tareas a ejecutar en paralelo
h1 = Thread(target = hilo1) #targetfuncion a ejecutar
h2 = Thread(target = hilo2)

h1.start()
#h1.join()
h2.start()
#h2.join()
#h1.join()# Espera a que termine el hilo para cerrar el proceso
time.sleep(2)
print('Termina el programa principal')
