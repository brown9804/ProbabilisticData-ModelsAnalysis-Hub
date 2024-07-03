# Ejemplo 2. 2
#Parte de la coincidencia de las placas
#Últimas cifras de las placas: Calcule la
#probabilidad de que se repitan las dos últimas cifras
#de la matrícula en quince automóviles anotados al azar.

#Utilizando el método de LA REGLA DE LAPLACE Y LA COMBINATORIA


#Recuerde que como es coincidencia de días nos fijamos en los 0-9  digitos qu tiene la placa = 10
print("\nEste programa funciona para calcular la coincidencia en los dos últimos digitos de una placa\n")
print("Se calcula para la segunda pregunta en el ejemlo 2.2 \n")
#probabilidad 1
probabilidad15 = 1.0
#personas presentes = asistentes en este caso son 50 para
carros = 15
print("Numero de placas analizadas (carros vistos):   ", carros)

#son dos digitos combinados 10x10
#calculando la probabilidad
for i in range(carros):
    probabilidad15 = probabilidad15 * (100-i)/100
print("\nProbabilidad de que coincida los dos últimos digitos de la placa es de {0:.2f}" .format(1 - probabilidad15))
