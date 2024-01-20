notas = []
while True:
    respuesta = input('Desea ingresar una nota\n Ingrese Y para ingresar o N para finalizar?')
    if respuesta == 'Y':
        nueva_nota = int(input('Ingrese una nota entre 1 y 10:'))
        if nueva_nota >= 1 and nueva_nota <= 10:
            notas.append(nueva_nota)
            total = sum(notas)
            cantidad = len(notas)
            promedio = total / cantidad
            print(f'La nota se ha agregado correctamente\n El promedio es: {promedio}')
        else:
            print(f'{nueva_nota} no es una nota válida')
    elif respuesta == 'N':
        print('Fin del programa')
        break
    else:
        print('Respuesta inválida')