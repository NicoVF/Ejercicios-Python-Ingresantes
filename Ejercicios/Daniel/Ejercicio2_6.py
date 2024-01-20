def par_impar(numero):
    if numero % 2 == 0:
        return 'par'
    else:
        return 'impar'
def cantidad_numeros(q_numero):
    q = len(str(q_numero))
    return q

def multiplo_10(multiplo):
    if (multiplo%10) != 0 :
        return multiplo-(multiplo%10)
    else:
        return multiplo
    
valor = int(input('Ingrese un valor para calcular si es par o impar, cuantos caracteres tiene y su multiplo de 10 inferior: '))

print(f'El número {valor} es: {par_impar(valor)}, tiene {cantidad_numeros(valor)} caracteres, y su multiplo de 10 inferior es: {multiplo_10(valor)}')