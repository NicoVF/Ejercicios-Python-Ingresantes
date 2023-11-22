'''Funcion para calcular el producto de dos elementos'''
def producto(a,b):
    return a*b

'''Programa'''
print("Hola, bienvenido al programa para multiplicar dos números\n")
numero1 = int(input("Ingrese por favor el primer número: "))
numero2 = int(input("\nIngrese por favor el segundo número: "))
print(f"\nEl resultado del producto de {numero1} y {numero2} es: {producto(numero1,numero2)}")