def validar_numero(n):
    calculo1 = n % 2
    contador = 0
    if calculo1 == 0:
        print(f'El número {n} es par')
    else:
        print(f'El número {n} es impar')
    for i in range(2, n + 1):
        if n % i == 0:
            contador += 1
    if contador == 1:
        print(f'El número {n} es primo')
    else:
        print(f'El número {n} no es primo')

validar_numero(16)
