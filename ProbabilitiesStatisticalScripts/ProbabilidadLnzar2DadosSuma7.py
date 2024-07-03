#Este es el ejemplo 2.1 en este se muestra la probabilidad de
#lanzar dos dados y que el resultado de la suma de estos de 7.

#forma de ejecutar
#python3 ProbabilidadLnzar2DadosSuma7.py

#Importando paquetes necesarios
from collections import defaultdict
#Creando diccionario con todas las combinaciones posibles y la suma de cada una
d = {(i,j) : i+j for i in range(1, 7) for j in range(1,7)}
#imprimiendo
print("\n")
print("Imprimiendo combinaciones posibles de los dados y suma de esta")
print("Lleva el siguiente formato (numero dado 1, numero dado 2):  suma dados\n")
print(d)

#creando un diccionario vacio para que cuando no se crea en el diccionario original
#en vez de error lo que haga sea crearlo, en otras palabras, es subconjento del diccionario original
#una vez que rellena para ser el conjunto universal
dinv = defaultdict(list)
#se imprime
print("\nConjunto complento:     ", dinv)


print('\nAntes de buscar las posibles permutaciones en las que puede suceder el resultado de 7...\n')
print(d.items())

#Realizando las permutaciones
for i,j in d.items():
        dinv[j].append(i)

print('\nDespués de realizar las distintas permutaciones obtenemos:\n')
print(dinv)
#se escoge de las permutaciones las que suman 7
print('\nCombinaciones que suman 7:  ', dinv[7])

print('\nElementos (cantidad de combinaciones):  ', len(dinv[7]))
#Calculando
probabilidades = {i : len(j)/36 for i,j in dinv.items()}

print('\nEl vector de probabilidades (probabilidad de cada número en salir cuando se lazan los dados) de suma es: \n', probabilidades)
print('\nLa probabilidad de que la suma sea 7 es =   ', probabilidades[7])
