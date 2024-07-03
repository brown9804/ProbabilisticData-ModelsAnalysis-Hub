#Resolución de problema placas y suma
#Ejemplo 2.2
###Las placas del país tienen tres letras y
##tres dígitos numéricos. En cierto juego, unos
##amigos apuestan un fresco de tamarindo para el primero
##que encuentre una placa cuyos dígitos numéricos suman:
## 10 para A(ndrea), 15 para B(renda) y 20 para C(arlos).
##¿Quién tiene más probabilidades de ganar?

##Forma de ejecutarlo
#python3 PlacasConSumaDigitosDeterminado.py

#Importando paquetes necesarios
from collections import defaultdict

#Creando diccionario con todas las combinaciones posibles y la suma de cada una
#dado que son 0-9 los numeros  y tres posibles
d = {(i,j) : i+j for i in range(0, 9) for j in range(0,9) for k in range(0,9)}

print("\n")
print("Imprimiendo combinaciones posibles de las placas y suma de esta")
print("Lleva el siguiente formato (Digito uno, Digito 2, Digito 3):  suma digites placa\n")
print(d)

#creando un diccionario vacio para que cuando no se crea en el diccionario original
#en vez de error lo que haga sea crearlo, en otras palabras, es subconjento del diccionario original
#una vez que rellena para ser el conjunto universal
dinv = defaultdict(list)
#se imprime
print("\nConjunto complento:     ", dinv)


print('\nAntes de buscar las posibles permutaciones\n')
print(d.items())

#Realizando las permutaciones
for i,j in d.items():
        dinv[j].append(i)

print('\nDespués de realizar las distintas permutaciones obtenemos:\n')
print(dinv)
#Calculando 10x10x10 = 1000
probabilidades = {i : len(j)/1000 for i,j in dinv.items()}
print('\nEl vector de probabilidades (probabilidad de cada número en salir en la placa: \n', probabilidades)

#se escoge de las permutaciones las que suman 10
print('\nCombinaciones que suman 10 (Andrea):  ', dinv[10])
print('\nElementos (cantidad de combinaciones) para la suma de 10:  ', len(dinv[10]))
print('\nLa probabilidad de que la suma sea 10 es =   ', probabilidades[10])


#se escoge de las permutaciones las que suman 15
print('\nCombinaciones que suman 15 (Brenda):  ', dinv[15])
print('\nElementos (cantidad de combinaciones) para la suma de 15:  ', len(dinv[15]))
print('\nLa probabilidad de que la suma sea 15 es =   ', probabilidades[15])

#se escoge de las permutaciones las que suman 20
print('\nCombinaciones que suman 20 (Carlos):  ', dinv[20])
print('\nElementos (cantidad de combinaciones) para la suma de 20:  ', len(dinv[20]))
if (len(dinv[20])==0):
    print('\nLa probabilidad de que la suma sea 20 es =  0')
else:
    print('\nLa probabilidad de que la suma sea 20 es =   ', probabilidades[20])





