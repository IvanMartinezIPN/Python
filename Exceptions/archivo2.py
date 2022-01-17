def divide(x,y):
    try:
        operation = x/y
    except (ZeroDivisionError,TypeError):
        print("No se puede dividir entre cero y no se aceptan caracteres")
    else:
    #else solo si no hubo ninguna exepcion
        return operation
    finally:
        print("Gracias por usar")
    #SIEMPRE SE EJECUTA

#try,finally y except precedencia de operadores

result = divide(10,5)
print(result)