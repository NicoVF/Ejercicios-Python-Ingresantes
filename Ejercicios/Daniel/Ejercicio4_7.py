numero = int(input("Ingrese un número entero: "))
romano = ''

while numero > 0:
    if numero >= 1000:
        romano += 'M'
        numero -= 1000
    elif numero >= 900:
        romano += 'CM'
        numero -= 900
    elif numero >= 500:
        romano += 'D'
        numero -= 500
    elif numero >= 400:
        romano += 'CD'
        numero -= 400
    elif numero >= 100:
        romano += 'C'
        numero -= 100
    elif numero >= 90:
        romano += 'XC'
        numero -= 90
    elif numero >= 50:
        romano += 'L'
        numero -= 50
    elif numero >= 40:
        romano += 'XL'
        numero -= 40
    elif numero >= 10:
        romano += 'X'
        numero -= 10
    elif numero >= 9:
        romano += 'IX'
        numero -= 9
    elif numero >= 5:
        romano += 'V'
        numero -= 5
    elif numero >= 4:
        romano += 'IV'
        numero -= 4
    elif numero >= 1:
        romano += 'I'
        numero -= 1

print(f'El número ingresado es: {romano}')
