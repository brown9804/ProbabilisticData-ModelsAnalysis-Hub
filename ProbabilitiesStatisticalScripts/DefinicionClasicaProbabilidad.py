####Parte 1
#Se considera una muestra, el cual es un vector con n elementos
print("Se posee la siguiente muestra: 1,2,3,4,5,6   ")
espacio_muestras = [1,2,3,4,5,6]
#cuenta la cantidad de elementos que posee la muestra
n = len(espacio_muestras)
#saca la probabilidad es dividir 1/cantidad de elementos
probabilidad = 1.0/n
print("La probabilidad es de:   ", probabilidad)
#se busca por los numeros par en la muestra de arriba, lo que
#calcula es la razon entonces divide el numero entre dos y si da
#numero entero entonces es par 4/2 = 2 250 /2 =125
numeros_pares = [i for i in espacio_muestras if i % 2 is 0]
#cuenta la cantidad de numeros pares
h = len(numeros_pares)
#considera la probabilidad de numero pares, cantidad de numeros pares/numero total
probabilidadpares = float(h)/n
print("Probabilidad de que salga un número par:   ", probabilidadpares)

