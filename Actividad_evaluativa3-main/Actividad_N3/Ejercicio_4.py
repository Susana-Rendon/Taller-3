import statistics

def nota():
    while True:
        try:
            notas = float(input("Ingrese su calificación debe estar entre 0 y 10: ")) #Para que el usuario ingrese el valor y no se salga dentro de ese rango
            if 0 <= notas <= 10:
                return notas
            else:
                print("La calificación debe estar entre 0 y 10. Intenta de nuevo.")
        except ValueError:
            print("Valor no válido. Por favor, ingresa un número.")

calificaciones = []

# Pedir 5 calificaciones al usuario
for i in range(5):
    calificacion = nota()
    calificaciones.append(calificacion)

suma_calificaciones = sum(calificaciones)
cantidad_calificaciones = len(calificaciones)

promedio = suma_calificaciones / cantidad_calificaciones #Sacamos el promedio con la suma de las notas ingresadas y la cantidad ingresada
calificaciones_ordenadas = sorted(calificaciones) # Para odenar las notas de forma ascendente
maxima = max(calificaciones_ordenadas) # Sacamos la maxima nota del estudiente
minima = min(calificaciones_ordenadas) # Sacamos la minima nota del estudiente
mediana = calificaciones_ordenadas[2]
desviacion_estandar = statistics.stdev(calificaciones_ordenadas)



print(f"Las calificaciones ingresadas son: {calificaciones_ordenadas}")
print(f"El promedio de sus calificaciones es: {promedio:.2f}")
print(f"La mediana de sus calificaciones es: {mediana}")
print(f"La desviacion estandar de sus calificaciones es: {desviacion_estandar:.2f}")
print(f"Su calificacion mas alta es: {maxima}")
print(f"Su calificacion mas baja es: {minima}")

if 9 <= promedio <= 10:
    print(f"Sus notas son excelentes")
elif 7 <= promedio <= 8.99:
        print(f"Sus notas son buenas")
elif 5 <= promedio < 6.99:
        print(f"Sus notas estan aprobadas")
elif  promedio <= 5:
        print("Esta reprobado")
else:
    print(f"Ingreso valor invalido")

if desviacion_estandar < 1:
    print("Las calificaciones son consistentes. Mantén tu enfoque actual.")
elif 1 <= desviacion_estandar <= 2:
    print("Hay algo de variabilidad en tus calificaciones. Podrías revisar áreas con notas más bajas para mejorar.")
else:
    print("Hay una alta variabilidad en tus calificaciones. Sería útil concentrarse más en las áreas con notas más bajas.")


