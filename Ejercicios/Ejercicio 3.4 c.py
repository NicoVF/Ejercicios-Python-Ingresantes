def producto_vectorial(x1,y1,z1,x2,y2,z2):
    x = y1*z2 - z1*y2
    y = z1*x2 - x1*z2
    z = x1*y2 - y1*x2
    print(f'El producto vectorial es: ({x},{y},{z})')

producto_vectorial(1,4,-2,3,-1,0)