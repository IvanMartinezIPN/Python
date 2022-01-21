#Hilos y semaforos

from concurrent.futures import thread
import threading
import random
import time

probadores = 3
#La cantidad maxima de hilos que pueden usar la funcion pasar
semaforo =  threading.Semaphore(probadores)

def pasar(i):
    tiempo = random.randint(0,1)
    time.sleep(tiempo)
    #Decrementar en 1 (reserva), por lo tanto ahora aceptara hilos hasta que probadores = 0
    semaforo.acquire()
    print('\nPersona {} entra al probador'.format(i))
    tiempo = random.randint(5,10) #esperamos un tiempo que varia entre 5 y 10
    time.sleep(tiempo)
    print('\nPersona {} ha terminado de usar el probador :'.format(i))
    #incrementa en 1 (libera) el valor de probadores, por lo tanto, puede aceptar mas hilos
    semaforo.release()


#Creamos tareas a ejecutar en paralelo

persona = threading.Thread(target = pasar, args=(1,))

persona2 = threading.Thread(target = pasar, args =(2,))
persona3 = threading.Thread(target = pasar, args =(3,))
persona4 = threading.Thread(target = pasar, args =(4,))

#iniciamos las tareas:

persona.start()
persona2.start()
persona3.start()
persona4.start()