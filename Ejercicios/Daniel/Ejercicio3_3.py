def maximo_producto(a,b,c,d):
    ab = a*b
    ac = a*c
    ad = a*d
    bc = b*c
    bd = b*d
    cd = c*d
    lista = [ab,ac,ad,bc,bd,cd]
    valor_maximo = max(lista)
    print(f'El valor máximo en la lista es: {valor_maximo}')

maximo_producto(1,5,-2,-4)