###Aplicacion del teorema de bayes
##Ejemplo 1
#Un moderno edificio (la Escuela de Ingeniería Eléctrica)
# tiene dos ascensores para uso de los estudiantes. El primero
#de los ascensores es usado el 45% de las ocasiones, mientras
#que el segundo es usado el resto de las ocasiones. El uso continuado
# de los ascensores provoca un 5% de fallos en el primero de los
# ascensores y un 8% en el segundo. Un día suena la alarma de uno de
# los ascensores porque ha fallado. Calcule la probabilidad de que
#haya sido el primero de los ascensores.


###forma de ejecutarlo
#### python3 FallosAscensoresTeoremaBayes.py

print(" Un primer acercamiento intuitivo a la solución nos dice que si el primero se usa menos veces y falla con menor porcentaje entonces la probabilidad de que haya sido el de la alarma será menor al 50 porciento  \n")

# Datos generales
p_ascensores = [0.45, 0.55]
p_fallo = [0.05, 0.08]

###
####Con [P(A), P(B)] = p_ascensores y
###[P(F|A), P(F|B)] = p_fallo, entonces
#           O
#          / \
#         /   \
#       P(A)  P(B)
#       /       \
#    P(F|A)   P(F|B)
#     /           \
#    F             F
#####

# Probabilidad total de fallar
p_fallar = sum([p_ascensores[i] * p_fallo[i] for i in range(len(p_ascensores))])

####
##Si P(F) = p_fallar es la probabilidad de fallar
###(y de que suene la alarma), entonces el teorema
###de Bayes queda como:
###
##         P(F|A) P(A)
##P(A|F) = -----------
##             P(F)
###

# Aplicación de Teorema de Bayes
p_bayes = [(p_fallo[i] * p_ascensores[i]) / p_fallar for i in range(len(p_ascensores))]
print("La probabilidad de que haya sido el primero de los ascensores es {A:0.2f}. Y el segundo {B:0.2f}".format(A=p_bayes[0]*100, B=p_bayes[1]*100))


