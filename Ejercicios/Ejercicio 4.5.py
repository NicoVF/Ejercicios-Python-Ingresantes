# a)
def anio_bisiesto(anio):
    a = anio%4
    b = anio%100
    c = anio%400
    if (a==0 and b!=0) or (c==0):
        print(f'El año {anio} es bisiesto')
    else:
        print(f'El año {anio} no es bisiesto')
    
# b)
def validar_fecha(dia,mes,año):
    dias_en_mes=[31,28,31,30,31,30,31,31,30,31,30,31]
    if mes<1 or mes>12:
        return False
    elif mes==2 and ((año%4==0 and año%100!=0)or(año%400==0)) and dia>=1 and dia<30:
        return True
    elif (dia<1 or dia>dias_en_mes[mes-1]):
        return False
    else:
        return True
    

