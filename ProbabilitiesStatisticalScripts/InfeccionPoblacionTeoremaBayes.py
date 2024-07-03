#Ejemplo 3.2
#Utilizando el teorema de Bayes
print("\nHay una ciudad de 50 000 habitantes, con la siguiente distribución de población: Niñas 11000 Niños 9000 Mujeres 16000 Hombres 14000. Hay también un reporte de 9000 casos de una nueva variedad de virus que-no-debe-ser-mencionada, distribuidos de la siguiente forma: Niñas 2000 Niños 1500 Mujeres 3000 Hombres 2500 ¿Está la probabilidad de contraer el virus relacionada con la pertenencia a un sector demográfico? Esto puede estudiarse analizando las probabilidades 𝑃(tener gripe∣pertenece a X sector\n")

#Forma de ejecutarlo
#python3 InfeccionPoblacionTeoremaBayes.py

#se calcula probailidad para cada sector de la poblacion no infectada
MuestraCiudad = 50000
NinasNaci = 11000
NinosNaci = 9000
MujeresNaci = 16000
HombresNaci = 14000

#Calculando La probabilidad de un evento A se define a priori
#(sin experimentación) como:
probabilidadNinasNaci = round((NinasNaci/MuestraCiudad),2)
probabilidadNinosNaci = round((NinosNaci/MuestraCiudad),2)
probabilidadMujeresNaci = round((MujeresNaci/MuestraCiudad),2)
probabilidadHombresNaci = round((HombresNaci/MuestraCiudad),2)

# print("Probibilidad de una niña en la ciudad: ", probabilidadNinasNaci )
# print("Probibilidad de una niño en la ciudad: ", probabilidadNinosNaci )
# print("Probibilidad de una mujer en la ciudad: ", probabilidadMujeresNaci )
# print("Probabilidad de hombre en la ciudad: ", probabilidadHombresNaci)
#se calcula probailidad Poblacion infectada
PoblacionInfectadaTotal = 9000

CasosNinas = 2000
CasosNinos = 1500
CasosMujeres = 3000
CasosHombres = 2500

#Calculando La probabilidad de un evento A se define a priori
#(sin experimentación) como:
probabilidadNinasInfec =  round((CasosNinas/PoblacionInfectadaTotal),2)
probabilidadNinosInfec = round((CasosNinos/PoblacionInfectadaTotal),2)
probabilidadMujeresInfec = round((CasosMujeres/PoblacionInfectadaTotal),2)
probabilidadHombresInfec = round((CasosHombres/PoblacionInfectadaTotal),2)

# print("Probibilidad de una niña infectada en la ciudad: ", probabilidadNinasInfec )
# print("Probibilidad de una niño infectado en la ciudad: ", probabilidadNinosInfec )
# print("Probibilidad de una mujer infectada en la ciudad: ", probabilidadMujeresInfec )
# print("Probabilidad de hombre infectado en la ciudad: ", probabilidadHombresInfec)



# Datos generales
p_nacimientos = [probabilidadNinasNaci, probabilidadNinosNaci, probabilidadMujeresNaci, probabilidadHombresNaci]
#p_nacimientos = [0.22, 0.18, 0.32, 0.28]
p_infectados = [probabilidadNinasInfec, probabilidadNinosInfec, probabilidadMujeresInfec, probabilidadHombresInfec]
#p_infectados = [0.22, 0.17, 0.33, 0.28]
###
####Con [P(A), P(B)] = p_nacimientos y
###[P(F|A), P(F|B)] = p_infectados, entonces
#           O
#          / \
#         /   \
#       P(A)  P(B)
#       /       \
#    P(F|A)   P(F|B)
#     /           \
#    F             F
#####

# Probabilidad total de infectarse
p_infeccion = sum([p_nacimientos[d] * p_infectados[d] for d in range(len(p_nacimientos))])

####
##Si P(F) = p_infectados es la probabilidad de infectarse
###(y de que se den cuenta), entonces el teorema
###de Bayes queda como:
###
##         P(F|A) P(A)
##P(A|F) = -----------
##             P(F)
###

# Aplicación de Teorema de Bayes
p_bayes = [(p_infectados[i]*p_nacimientos[i]) / p_infeccion for i in range(len(p_nacimientos))]
print("La probibilidad de infección de en niñas es {A:0.2f}, el niños {B:0.2f}, el mujeres {C:0.2f} y el de hombres {D:0.2f}".format(A=p_bayes[0]*100, B=p_bayes[1]*100, C=p_bayes[2]*100, D=p_bayes[3]*100))
