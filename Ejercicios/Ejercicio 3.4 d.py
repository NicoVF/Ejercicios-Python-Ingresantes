import math

def coordenadas_a_norma(x,y,z):
    return math.sqrt((x**2)+(y**2)+(z**2))

def coordenadas_diferencia(x1,y1,z1,x2,y2,z2):
    return x1-x2, y1-y2, z1-z2

def producto_vectorial(x1,y1,z1,x2,y2,z2):
    x = y1*z2 - z1*y2
    y = z1*x2 - x1*z2
    z = x1*y2 - y1*x2
    return x, y, z

def area_triangulo(x1,y1,z1,x2,y2,z2,x3,y3,z3):
    a1, a2, a3 = coordenadas_diferencia(x2, y2, z2, x1, y1, z1)
    b1, b2, b3 = coordenadas_diferencia(x3, y3, z3, x1, y1, z1)
    
    c1, c2, c3 = producto_vectorial(a1,a2,a3,b1,b2,b3)
    
    area_doble = coordenadas_a_norma(c1,c2,c3)
    
    return area_doble / 2

print(area_triangulo(5,8,-1,-2,3,4,-3,3,0))