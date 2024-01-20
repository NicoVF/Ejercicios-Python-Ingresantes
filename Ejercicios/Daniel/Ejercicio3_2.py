def convertir_a_segundos(hora):
    h, m, s = map(int, hora.split(':'))
    return h * 3600 + m * 60 + s

def convertir_a_hora(segundos):
    h = segundos // 3600
    m = (segundos % 3600) // 60
    s = (segundos % 3600) % 60
    return f'{int(h):02d}:{int(m):02d}:{int(s):02d}'


hora = input('Ingrese una hora con el siguiente formato "hh:mm:ss": ')
segundos = int(input('Ingrese la cantidad de segundos que desea calcular: '))
print(f'Las horas ingresadas: {hora}')
print(f'Convertido en segundos es: {convertir_a_segundos(hora)}')
print(f'Los segundos ingresados: {segundos}')
print(f'Convertido en horas es: {convertir_a_hora(segundos)}')
