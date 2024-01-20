# a)
def anio_bisiesto_mensaje(anio):
    a = anio%4
    b = anio%100
    c = anio%400
    if (a==0 and b!=0) or (c==0):
        print(f'El año {anio} es bisiesto')
    else:
        print(f'El año {anio} no es bisiesto')
        
def anio_bisiesto(anio):
    a = anio%4
    b = anio%100
    c = anio%400
    if (a==0 and b!=0) or (c==0):
        return True
    else:
        return False
    
# b)

def dias_del_mes(mes, anio):
    dias_en_mes=[31,28,31,30,31,30,31,31,30,31,30,31]
    if anio_bisiesto(anio) and mes == 2:
        return 29
    else:
        return dias_en_mes[mes-1]
    
# c)
def validar_fecha(dia, mes, anio):
    dias_en_mes = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    if anio_bisiesto(anio) and mes == 2:
        dias_en_mes[1] = 29
    elif mes < 1 or mes > 12 or dia < 1 or dia > dias_en_mes[mes - 1]:
        return False
    else:
        return True
    
def verificar_fecha():
    dia = int(input("Ingresa el día: "))
    mes = int(input("Ingresa el mes: "))
    anio = int(input("Ingresa el año: "))
    
    if validar_fecha(dia, mes, anio):
        print(f"La fecha {dia}/{mes}/{anio} es válida.")
    else:
        print(f"La fecha {dia}/{mes}/{anio} no es válida.")
        
# d)
def dias_hasta_eomonth():
    dia=int(input("Dia del mes actual: "))
    mes=int(input("Mes actual: "))
    anio=int(input("Año actual: "))
    
    if validar_fecha(dia, mes, anio):
        if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
            dias = 31 - dia
            print(f'Faltan {dias} para terminar el mes')
        elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
            dias = 30 - dia
            print(f'Faltan {dias} para terminar el mes')
        elif anio_bisiesto(anio) and mes == 2:
            dias = 29 - dia
            print(f'Faltan {dias} para terminar el mes')
        else:
            dias = 28 - dia
            print(f'Faltan {dias} para terminar el mes')


# e)

def dias_hasta_eoyear():
    dia = int(input("Ingresa el día: "))
    mes = int(input("Ingresa el mes: "))
    anio = int(input("Ingresa el año: "))
    dias_en_mes = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    if anio_bisiesto(anio):
        dias_en_mes[1] = 29
    if validar_fecha(dia, mes, anio):
        dias_totales = sum(dias_en_mes)
        dias_pasados = sum(dias_en_mes[:mes-1]) + dia
        dias_restantes = dias_totales - dias_pasados
        print(f'Faltan {dias_restantes} días para terminar el año.')
    else:
        print("La fecha ingresada no es válida.")
        
# f)

def dias_hasta_fecha():
    dia = int(input("Ingresa el día: "))
    mes = int(input("Ingresa el mes: "))
    anio = int(input("Ingresa el año: "))
    dias_en_mes = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    if anio_bisiesto(anio):
        dias_en_mes[1] = 29
    if validar_fecha(dia, mes, anio):
        dias_pasados = sum(dias_en_mes[:mes-1]) + dia
        print(f'Pasaron {dias_pasados} días que comenzó el año.')
    else:
        print("La fecha ingresada no es válida.")
        
# g)

def tiempo_transcurrido(dia1, mes1, anio1, dia2, mes2, anio2):
    dias_en_mes = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    dias_en_mes2 = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    if not validar_fecha(dia1, mes1, anio1) or not validar_fecha(dia2, mes2, anio2):
        return "Una o ambas fechas no son válidas."
    
    if anio_bisiesto(anio1):
        dias_en_mes[1] = 29
    dias_pasados1 = sum(dias_en_mes[:mes1-1]) + dia1
    

    if anio_bisiesto(anio2):
        dias_en_mes2[1] = 29
    dias_pasados2 = sum(dias_en_mes[:mes2-1]) + dia2
    
    dias_transcurridos = dias_pasados2 + (anio2 - anio1) * 365 - dias_pasados1
    
    anios = dias_transcurridos // 365
    dias_transcurridos %= 365
    meses = dias_transcurridos // 30
    dias_transcurridos %= 30
    dias = dias_transcurridos
    
    print(f'El tiempo transcurrido es de {anios} años, {meses} meses y {dias} días')
    
