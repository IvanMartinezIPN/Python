import sys

def BMI(altura : float, peso : float):
    try:
        if (altura < 1 or peso < 1):
            raise ValueError('El valor debe ser mayor a cero 0')
        indice = peso / altura**2  #potencia
    except (TypeError,ValueError,Exception,ArithmeticError) as e:
        print(f'Error: {e}')
    else:
        return indice
    finally:
        print('Los valores ingresados son correctos')

def BMI_indice(bmi : float):
    try:
        indice_bmi = ''
        if bmi < 1:
            raise ValueError('BMI no es valido')
        elif bmi < 18.5:
            indice_bmi = 'Bajo peso'
        elif bmi >= 18.5 and bmi <= 24.9:
            indice_bmi = 'Saludable'
        else:
            indice_bmi = 'Sobrepeso' 
    except (TypeError,ValueError,Exception) as e:
        print(f'Error: {e}')
    else:
        return indice_bmi
    finally:
        print('Los valores ingresados son correctos')


if __name__ == "__main__":
    #altura
    try:
        altura = float(input("Altura en metros: "))
        if altura < 0:
            raise ValueError('La altura debe ser mayor a 0 metros')
    except (TypeError,ValueError,Exception) as e:
        print(f'Error: {e}')
    #peso
    try:
        peso = float(input("Peso en kilogramos: "))
        if peso < 0:
            raise ValueError('El peso debe ser mayor a 0 kg')
    except (TypeError,ValueError,Exception) as e:
        print(f'Error: {e}')
    bmi = BMI(altura, peso)
    indice_bmi = BMI_indice(bmi)
    print(f'BMI: {bmi} Resultado: {indice_bmi}')
    pass