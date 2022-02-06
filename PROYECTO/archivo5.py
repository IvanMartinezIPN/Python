from threading import Thread
import time
def rec_fib(n):
    if n > 1:
        return rec_fib(n-1) + rec_fib(n-2)
    return n
def incremento(n):
    for i in range(0, limite + 1, 1):
     print(i)
     time.sleep(1.0)
limite = int(input('Ingresa el numero de la serie de fibonacci:'))
for i in range(limite):
    print(rec_fib(i))
limite2 = int(input('Ingresa el numero de la serie de fibonacci:'))
incremento(limite2)
hilo1 = Thread(target=rec_fib, args=(1,))
hilo2 = Thread(target=incremento, args=(2,))
hilo1.start()
hilo2.start()
hilo2.join()
print("Programa terminado")