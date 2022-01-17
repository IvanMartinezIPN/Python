#raise es para lanzar una excepcion si ocurre una condicion, la declaracion se puede complmentar
#con una exepcion personalizada
from typing import Type
def divide(x,y):
    try:
        operation = x/y
    except (ZeroDivisionError,TypeError):
        print("No se puede dividir entre cero y no se aceptan caracteres")
        try:
            resultado2 = 10/'b'
        except TypeError:
            print("Error en el segundo bloque")
    else:
    #else solo si no hubo ninguna exepcion
        return operation
    finally:
        print("Gracias por usar")
    #SIEMPRE SE EJECUTA
    #finally puede cachar errores dentro de otros bloques como except y else
#try,finally y except precedencia de operadores

result = divide(10,0)
print(result)