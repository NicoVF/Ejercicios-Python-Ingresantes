import random
lista = []
def imprimir_domino():
    print('Imprimiendo fichas')
    for i in range(1,7):
        for j in range (1,7):
            lista.append(f'{i}-{j}')
            print(f'{i}-{j}')

imprimir_domino()
n=int(input('Ingresá la cantidad de fichas que deseas: '))
print(random.sample(lista, n))