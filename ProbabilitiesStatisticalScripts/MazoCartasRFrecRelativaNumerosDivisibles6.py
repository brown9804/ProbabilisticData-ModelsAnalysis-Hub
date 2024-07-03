####Parte 2 ejemplo de naipe con 52 cartas probabilidad de sacar 6 con 4 palos 
# Crear espacio de muestras de palo, es decir un mazo de reinas,
#diamantes, etc en total son 4

#Forma de ejecutarlo 
#python3 MazoCartasRFrecRelativaNumerosDivisibles6.py

palo = [i+1 for i in range(13)]
# Comprobar divisibilidad por 6
divisible_6 = [i for i in palo if i % 6 is 0]
print("Tomando en cuenta que hay cuatro palos, la frecuencia relativa de los números divisibles por 6 es:")
#Saca la probabilidad de que salga 6
probabilidad_6 = (4*float(len(divisible_6)))/(4*len(palo))
# Respuesta frecuencia relativa de los números divisibles por 6 es
print("{0:0.2f}".format(probabilidad_6))


