def convertir_fahrenheit_celcius(c):
    return 9/5*c + 32


print('Programa para convertir de grados Celcius a Fahrenheit')
celcius = float(input('Ingrese los grados Celcius: '))


print(f'Usted ingresó {celcius}° Celcius, su equivalente en Fahrenheit es {convertir_fahrenheit_celcius(celcius)}°')