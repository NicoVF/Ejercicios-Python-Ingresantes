'''
Ejercicio 1.2. Utilizando la función del ejercicio anterior, escribir un programa (un archivo .py)
que pida al usuario dos números, y luego muestre el producto.
'''

def producto(a,b):
    return a*b

print("Que numeros quiere multiplicar?\n")
a = int (input("Ingrese primer número: "))
b = int (input("Ingrese el segundo número: "))
print(f"\nResultado de {a} x {b} es: {producto(a,b)}")