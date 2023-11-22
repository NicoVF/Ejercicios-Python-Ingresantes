def calculo_factorial(valor):
    if valor == 0:
        return 0
    else:
        calculo = 1
        for i in range(1,valor+1):
            calculo = calculo * i
        return calculo

def factoriales_multiples(lista_factoriales):
    for i in range(len(lista_factoriales)):
        print(f'Posición: {i+1} - Valor: {lista_factoriales[i]} - Factorial: {calculo_factorial(lista_factoriales[i])}')

lista = []
print('Ingrese los valores uno a uno sobre los que se quiera calcular factoriales, cuando no desee ingresar más escriba "Salir": ')
while True:
    a = input()
    if a.lower() == "salir":
        break
    else:
        lista.append(int(a))

factoriales_multiples(lista)
