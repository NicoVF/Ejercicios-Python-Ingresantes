def convertir_fahrenheit_celcius(f):
    return (f-32)*(5/9)

def tabla_convertir_temperaturas():
    for i in range(13):
        print("Fahrenheit: ",i*10," Celsius: ",convertir_fahrenheit_celcius(i*10))

print(tabla_convertir_temperaturas())
