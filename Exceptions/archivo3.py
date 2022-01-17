#raise es para lanzar una excepcion si ocurre una condicion, la declaracion se puede complmentar
#con una exepcion personalizada
def divide(x,y):
    try:
        operation = x/y
        if operation <0:
            raise ValueError("No se aceptan negativos")
    except ValueError as numNegativo:
        print("numNegativo")
    except (ZeroDivisionError,TypeError):
        print("No se puede dividir entre cero y no se aceptan caracteres")
    else:
    #else solo si no hubo ninguna exepcion
        return operation
    finally:
        print("Gracias por usar")
    #SIEMPRE SE EJECUTA
    #finally puede cachar errores dentro de otros bloques como except y else
#try,finally y except precedencia de operadores

result = divide(10,-5)
print(result)