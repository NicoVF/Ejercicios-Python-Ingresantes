def imprimir_matriz_identidad(n):

    matriz_identidad = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        matriz_identidad[i][i] = 1

    for fila in matriz_identidad:
        print(fila)


valor = int(input("Ingrese un valor para genrar una matriz identidad: "))

imprimir_matriz_identidad(valor)
