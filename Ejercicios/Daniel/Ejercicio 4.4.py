import cmath
def max_min_polinomio(a, b, c):
    # Calcular el vértice
    xv = -b / (2*a)
    # Se reemplaza en la función polinómica (ax^2+bx+c) el valor de x por xv, eso nos da yv
    yv = (a * xv**2) + (b * xv) + c

    # En un polinómio de grado 2 si a > 0 la función es concava para "arriba"
    # Si es a < 0 la función es concaba para "abajo"
    # Si a = 0 entonces es una función lineal
    if a > 0:
        print(f'El mínimo del polinomio se encuentra en el punto ({xv}, {yv})')
    elif a < 0:
        print(f'El máximo del polinomio se encuentra en el punto ({xv}, {yv})')
    else:
        print('El coeficiente a debe ser diferente de cero')

def calcular_raices(a, b, c):
    # Se calcula si la raíz de la fórmula resolvente da negativo o positivo
    calculo = b**2 - 4*a*c

    if a == 0:
        print("Si a es igual a 0 no es una función de polinomio grado 2")
    else:
        # Calcular las raíces
        if calculo >= 0:
            # Raíces reales
            x1 = (-b + (calculo)**(1/2)) / (2*a)
            x2 = (-b - (calculo)**(1/2)) / (2*a)
        elif calculo < 0:
            # Raíces complejas
            x1 = (-b + cmath.sqrt(calculo)) / (2*a)
            x2 = (-b - cmath.sqrt(calculo)) / (2*a)

        print(f"Las raíces del polinomio son {x1} y {x2}")

def interseccion_rectas(m1, b1, m2, b2):
    # Verificar si las pendientes son iguales
    if m1 == m2:
        if b1 == b2:
            print('Las rectas son coincidentes')
        else:
            print('Las rectas son paralelas')
    else:
        # Calcular el punto de intersección
        x = (b2 - b1) / (m1 - m2)
        y = m1 * x + b1
        print(f'Las rectas tienen intersección en {x} del eje X y en {y} del eje Y')

print("Calculos de funciones de grado dos")
a = float(input("Ingrese el valor del coeficiente a: "))
b = float(input("Ingrese el valor del coeficiente b: "))
c = float(input("Ingrese el valor del coeficiente c: "))
print("Calculo de intersección de dos rectas")
m1 = float(input("Ingrese el valor de la pendiente de la primer recta: "))
b1 = float(input("Ingrese el valor del término independiente de la primer recta: "))
m2 = float(input("Ingrese el valor de la pendiente de la segunda recta: "))
b2 = float(input("Ingrese el valor del término independiente de la primer recta: "))
max_min_polinomio(a,b,c)
calcular_raices(a,b,c)
interseccion_rectas(m1, b1, m2, b2)
print("Fin del programa")