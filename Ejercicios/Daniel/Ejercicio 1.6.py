
def suma_resta_division_multiplicacion(a,b):
    suma = a + b
    print(f'La suma de los elementos {a} y {b} da: {suma}')
    resta = a - b
    print(f'La resta de los elementos {a} y {b} da: {resta}')
    if b != 0:
        division = a / b
        print(f'La división de los elementos {a} y {b} da: {division}')
    else:
        division="No se puede dividir por 0"
    multiplicacion = a * b
    print(f'La multiplicación de los elementos {a} y {b} da: {multiplicacion}')

def tabla_multiplicar(n):
    for i in range(1,11):
        print (f'{n} x {i} = {n*i}')

suma_resta_division_multiplicacion(1,2)
tabla_multiplicar(4)