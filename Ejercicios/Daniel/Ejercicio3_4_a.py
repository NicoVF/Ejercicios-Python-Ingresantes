import math
def coordenadas_a_norma(x,y,z):
    norma_del_vector = math.sqrt((x**2)+(y**2)+(z**2))
    print(f'La norma del vector con coordenadas ({x},{y},{z}) es: {norma_del_vector}')

coordenadas_a_norma(3,2,-4)
