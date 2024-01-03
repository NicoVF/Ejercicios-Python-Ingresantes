'''
Ejercicio 1.3. Escribir funciones que permitan:
a) Calcular el perímetro de un rectángulo dada su base y su altura.
b) Calcular el área de un rectángulo dada su base y su altura.
c) Calcular el área de un rectángulo (alineado con los ejes x e y) dadas sus coordenadas
x1, x2, y1, y2.
d) Calcular el perímetro de un círculo dado su radio.
e) Calcular el área de un círculo dado su radio.
f) Calcular el volumen de una esfera dado su radio.
g) Dados los catetos de un triángulo rectángulo, calcular su hipotenusa.
'''
import math


def perimetroRectangulo(altura, base):
        return (altura * 2) + (base * 2)

print(perimetroRectangulo(4,5))


def areaRectangulo(altura, base):
    return altura * base

print(areaRectangulo(4,5))

def areaRectanguloCoordenadas(x1,x2,y1,y2):
    return (x2 - x1) * (y1 - y2)

print(areaRectanguloCoordenadas(4,3,2,5))

def perimetroCirculo(radio):
    return radio * 3.14159 * 2

print(perimetroCirculo(4))

def areaCirculo(radio):
    return (radio ** 2) * 3.14159

print(areaCirculo(4))

def volumenEsfera(radio):
    return 0.75 * 3.14159 * (radio ** 3)

print(volumenEsfera(4))

def calularhipotenusa(c1, c2):
    return c1 * c2

print(calularhipotenusa(4,3))