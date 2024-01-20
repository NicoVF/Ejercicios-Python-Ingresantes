def interes(C,x,n):
    return C * ((1+(x/100))**n)

print('Sistema de calculo de intereses anuales')
capital = int(input('Ingrese el capital: '))
intereses = float(input("Ingrese la tasa de interés anual: "))
tiempo_anios = int(input("Ingrese los años a calcular: "))

print(f'El capital con el interes ganado es: {interes(capital,intereses,tiempo_anios)}')