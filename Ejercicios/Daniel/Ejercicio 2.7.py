def numeros_triangulares(n):
    contador = 0
    for i in range (1, n+1):
        contador = contador + i
        print(f'{i} - {contador}')
        
        
valor = int(input('Ingrese un valor: '))
numeros_triangulares(valor)





