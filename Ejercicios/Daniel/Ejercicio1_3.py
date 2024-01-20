import math

'''a'''
def perimeto_rectangulo(base,altura):
    return (base * 2) + (altura * 2)

'''b'''
def area_rectangulo(base,altura):
    return base * altura

'''c'''
def area_rectangulo_puntos(x1,x2,y1,y2):
    return (x2 - x1) * (y2 - y1)

'''d'''
def perimetro_ciculo(radio):
    return radio * math.pi * 2

'''e'''
def area_circulo(radio):
    return math.pi * (radio ** 2)

'''f'''
def volumen_ciculo(radio):
    return 4/3 * math.pi * (radio**3)

'''g'''
def calculo_hipotenusa(cateto1,cateto2):
    return ((cateto1 ** 2) + (cateto2 ** 2)) ** (1/2)