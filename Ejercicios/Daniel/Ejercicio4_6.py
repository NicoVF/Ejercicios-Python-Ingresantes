while True:
    valor = int(input("Ingrese el día del año entre 1 y 366 para saber que día de la semana es: "))
    resto_semana = valor % 7

    if valor < 1:
        print("El valor ingresado no puede ser menor a 1")
    elif valor > 366:
        print("El valor ingresado no puede ser mayor a 366")
    else:
        if resto_semana == 1:
            print("Ese día fue un lunes")
        elif resto_semana == 2:
            print("Ese día fue un martes")
        elif resto_semana == 3:
            print("Ese día fue un miercoles")
        elif resto_semana == 4:
            print("Ese día fue un jueves")
        elif resto_semana == 5:
            print("Ese día fue un viernes")
        elif resto_semana == 6:
            print("Ese día fue un sábado")
        elif resto_semana == 7:
            print("Ese día fue un domingo")
        break
