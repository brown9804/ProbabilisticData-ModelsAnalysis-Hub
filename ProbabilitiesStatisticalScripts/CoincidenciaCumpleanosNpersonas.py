# Ejemplo 2. 3
#La coincidencia de cumpleaños:
###En una fiesta a la que concurren un total de 50 personas,
## una amiga intrépida afirma que en la fiesta debe haber por
#lo menos dos personas que cumplen años el mismo día. ¿Deberíamos creerle?

#Utilizando el método de LA REGLA DE LAPLACE Y LA COMBINATORIA


#Recuerde que como es coincidencia de días nos fijamos en los 365  días que tiene el año
print("\nEste programa funciona para calcular la coincidencia en el día de cumpleaños en un evento con N personas\n")
print("Inicialmente se calcula para la primera pregunta en el ejemlo 2.3 \n")
#probabilidad 1
probabilidad50 = 1.0
#personas presentes = asistentes en este caso son 50 para
asistentes = 50
print("Numero de asistentes en la fiesta:   ", asistentes)

#calculando la probabilidad
for i in range(asistentes):
    probabilidad50 = probabilidad50 * (365-i)/365
print("\nProbabilidad de que coincida una misma fecha de cumpleaños es {0:.2f}" .format(1 - probabilidad50))

npersonasAsistentes = int(input("Digite el número personas asistentes a la fiesta:\n"))
probabilidadN = 1.0
print("\nCorroborando internamente el número de asistentes:   ", npersonasAsistentes)


for iterador in range(npersonasAsistentes):
    probabilidadN = probabilidadN * (365-iterador)/365
print("\nProbabilidad de que coincida una misma fecha de cumpleaños es {0:.2f}" .format(1 - probabilidadN))
