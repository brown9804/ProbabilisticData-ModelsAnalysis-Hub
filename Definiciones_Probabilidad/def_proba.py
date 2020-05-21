#python3

#Para ejecutarlo digite, en el path donde se encuentra el archivo, por medio de la consola o terminal
# PATH$ python3 def_proba.py


#                  Modelos Probabilísticos de Senales y Sistemas
# Belinda Brown Ramírez
# Mayo, 2020
# timna.brown@ucr.ac.cr




#                   Tema: Introduccion a la probabilidad

#         Situación
# En el archivo lote.csv están los resultados de la inspección de N elementos de un lote
# de producción, donde se registró la presencia de características denominadas A, B, C y D,
# y donde "0" representa que no tiene esta característica y "1" que sí la tiene.

#        Cálculos
#1. ¿Cuál es la probabilidad de ocurrencia de cada característica?

#2. En todos los pares posibles, ¿cuál es la probabilidad de una característica dado otra? Ejemplo: P(C | D)

#3. ¿Hay relaciones de dependencia o independencia entre las características? ¿De qué tipo?

#4. Si hay una característica tipo D, ¿cuál es la probabilidad de que también tenga la característica A?



####   ****************         Algoritmo

# IMPORTANDO PAQUETES
import csv

# Obteniendo la informacion del lote.cvs
with open("lote.csv", "r") as csv_file:
    # Leyendo cada celda y separandola con coma para poder interpretar los datos
    csv_reader = csv.reader(csv_file, delimiter=',')
    # Se salta la primera linea del CSV
    next(csv_reader)
    # Inicializando los contadores
    n_total = -1 # debido a que hay que restarle la fila que se omite la cual contiene los encabezados
    A_ofn_total = 0
    B_ofn_total = 0
    C_ofn_total = 0
    D_ofn_total = 0
    #Arerglos para guardar datos de cada caracteristicas
    A_data = []
    B_data = []
    C_data = []
    D_data = []
    # Recorre todas las filas dentro del archivo cvs
    for filas_completas_data in csv_reader:
        #Cada vez que imprime una fila, suma entonces permite saber cuantas hay en total
        n_total = n_total + 1
        # Se imprime las filas completas para verificar
        #print(filas_completas_data)
        # Se guardan los datos en un arreglo
        # Dado que si contamos la cantidad de elementos por fila y sabemos que el encabezado
        # se designa de la siguiente manera n A B C D partiendo que n es la posicion cero
        A_data.append(filas_completas_data[1])
        B_data.append(filas_completas_data[2])
        C_data.append(filas_completas_data[3])
        D_data.append(filas_completas_data[4])
    # CREANDO DEFINCIONES PARA CALCULAS SIMULTANEADAD
    # Con el fin de calculas las probabilidades de una caracteristica dada la otra, se requieren realizar uso cálculos previos los cuales se
    # desarrollaran a continuación siendo utilizados en las ecuaciones finales para calcular la punto dos
    # Para de A
    def simultaneadadAB():
        # Definimos las variables para llevar la cuenta de las simultaneidad entre pares
        absuma = 0
        n_parafor = n_total +1
        for n in range(n_parafor):
            if A_data[n] == "1" and B_data[n] == "1":
                absuma =absuma +1
        return absuma
    def simultaneadadAC():
        acsuma = 0
        n_parafor = n_total +1
        for n in range(n_parafor):
            if A_data[n] == "1" and C_data[n] == "1":
                acsuma =acsuma +1
        return acsuma
    def simultaneadadAD():
        adsuma = 0
        n_parafor = n_total +1
        for n in range(n_parafor):
            if A_data[n] == "1" and D_data[n] == "1":
                adsuma =adsuma +1
        return adsuma
    # Para de B
    def simultaneadadBA():
        basuma = 0
        n_parafor = n_total +1
        for n in range(n_parafor):
            if B_data[n] == "1" and A_data[n] == "1":
                basuma =basuma +1
        return basuma
    def simultaneadadBC():
        bcsuma = 0
        n_parafor = n_total +1
        for n in range(n_parafor):
            if B_data[n] == "1" and C_data[n] == "1":
                bcsuma =bcsuma +1
        return bcsuma
    def simultaneadadBD():
        bdsuma = 0
        n_parafor = n_total +1
        for n in range(n_parafor):
            if B_data[n] == "1" and D_data[n] == "1":
                bdsuma =bdsuma +1
        return bdsuma
    # Para de C
    def simultaneadadCA():
        casuma = 0
        n_parafor = n_total +1
        for n in range(n_parafor):
            if C_data[n] == "1" and A_data[n] == "1":
                casuma =casuma +1
        return casuma
    def simultaneadadCB():
        cbsuma = 0
        n_parafor = n_total +1
        for n in range(n_parafor):
            if C_data[n] == "1" and B_data[n] == "1":
                cbsuma =cbsuma +1
        return cbsuma
    def simultaneadadCD():
        cdsuma = 0
        n_parafor = n_total +1
        for n in range(n_parafor):
            if C_data[n] == D_data[n]:
                cdsuma =cdsuma +1
        return cdsuma
    # Para de D
    def simultaneadadDA():
        dasuma = 0
        n_parafor = n_total +1
        for n in range(n_parafor):
            if D_data[n] == "1" and A_data[n]  == "1":
                dasuma =dasuma +1
        return dasuma
    def simultaneadadDB():
        dbsuma = 0
        n_parafor = n_total +1
        for n in range(n_parafor):
            if D_data[n] == "1" and B_data[n] == "1":
                dbsuma =dbsuma +1
        return dbsuma
    def simultaneadadDC():
        dcsuma = 0
        n_parafor = n_total +1
        for n in range(n_parafor):
            if D_data[n] == "1" and C_data[n] == "1":
                dcsuma =dcsuma +1
        return dcsuma
    # Se verifica por fila cuando sucede el evento A y B simultaneamente
    simAB = simultaneadadAB()
    # Sucede A y C simultaneamente
    simAC = simultaneadadAC()
    # Sucede A y D simultaneamente
    simAD = simultaneadadAD()
    # Se verifica por fila cuando sucede el evento B y A simultaneamente
    simBA = simultaneadadBA()
    # Sucede B y C simultaneamente
    simBC = simultaneadadBC()
    # Sucede B y D simultaneamente
    simBD = simultaneadadBD()
    # Se verifica por fila cuando sucede el evento C y A simultaneamente
    simCA = simultaneadadCA()
    # Sucede C y B simultaneamente
    simCB = simultaneadadCB()
    # Sucede C y D simultaneamente
    simCD = simultaneadadCD()
    # Se verifica por fila cuando sucede el evento D y A simultaneamente
    simDA = simultaneadadDA()
    # Sucede D y B simultaneamente
    simDB = simultaneadadDB()
    # Sucede D y C simultaneamente
    simDC = simultaneadadDC()
    # Ahora veamos cuantas caracteristicas hay
    for verifA in A_data:
        if verifA == "1":
            A_ofn_total = A_ofn_total +1
    for verifB in B_data:
        if verifB == "1":
            B_ofn_total = B_ofn_total +1
    for verifC in C_data:
        if verifC == "1":
            C_ofn_total = C_ofn_total +1
    for verifD in D_data:
        if verifD == "1":
            D_ofn_total = D_ofn_total +1
    # Con el fin de verificar la cantidad de filas se imprime
    print("La cantidad de toma de datos es de:      ", n_total)
    print("La cantidad de veces en las que sí hay \n característica A en la cantidad total de datos es:                       ", A_ofn_total)
    print("La cantidad de veces en las que sí hay \n característica B en la cantidad total de datos es:                       ", B_ofn_total)
    print("La cantidad de veces en las que sí hay \n característica C en la cantidad total de datos es:                       ", C_ofn_total)
    print("La cantidad de veces en las que sí hay \n característica D en la cantidad total de datos es:                       ", D_ofn_total, "\n")

####### A esta altura tenemos los datos necesarios para calcular la seccion 1.
# 1. ¿Cuál es la probabilidad de ocurrencia de cada característica?
# Se calcula como la cantidad de veces en las que sucede la caracteristica, dividida entre la muestra de datos total
probabilidadA = A_ofn_total/n_total
probabilidadB = B_ofn_total/n_total
probabilidadC = C_ofn_total/n_total
probabilidadD = D_ofn_total/n_total
# Respondiendo
print("Probabilidad ocasional A:              ", probabilidadA)
print("Probabilidad ocasional B:              ", probabilidadB)
print("Probabilidad ocasional C:              ", probabilidadC)
print("Probabilidad ocasional D:              ", probabilidadD, "\n")
                    ##
                    ##
                    ##
#2. En todos los pares posibles, ¿cuál es la probabilidad de una característica dado otra? Ejemplo: P(C | D)
# Hay que considerar que la probabilidad de que suceda una caracteristica dada la otra, se debe notar que es cuando
# en la toma de datos la característica sucede simultaneamente, por lo que debe ser un análisis por fila y si suceden
# ambas características entre la ocurrencia de la causante.
#Sabemos que como son 4 caracteristicas, hay doce posibles combinaciones en par entre ellas
# #1 P(A|B) = (P(A)*P(B))/P(B)    * se lee probabilidad de A debido a B
probabilidadAB = simAB/B_ofn_total
# #2 P(A|C) ...
probabilidadAC = simAC/C_ofn_total
# #3 P(A|D) ...
probabilidadAD = simAD/D_ofn_total
# #4 P(B|A) ...
probabilidadBA = simBA/A_ofn_total
# #5 P(B|C) ...
probabilidadBC = simBC/C_ofn_total
# #6 P(B|D) ...
probabilidadBD = simBD/D_ofn_total
# #7 P(C|A) ...
probabilidadCA = simCA/A_ofn_total
# #8 P(C|B) ...
probabilidadCB = simCB/B_ofn_total
# #9 P(C|D) ...
probabilidadCD = simCD/D_ofn_total
# #10 P(D|A) ...
probabilidadDA = simDA/A_ofn_total
# #11 P(C|A) ...
probabilidadDB = simDB/B_ofn_total
# #11 P(C|A) ...
probabilidadDC = simDC/C_ofn_total
print("P(A|B) =                 ",probabilidadAB)
print("P(A|C) =                 ",probabilidadAC)
print("P(A|D) =                 ",probabilidadAD)
print("P(B|A) =                 ",probabilidadBA)
print("P(B|C) =                 ",probabilidadBC)
print("P(B|D) =                 ",probabilidadBD)
print("P(C|A) =                 ",probabilidadCA)
print("P(C|B) =                 ",probabilidadCB)
print("P(C|D) =                 ",probabilidadCD)
print("P(D|A) =                 ",probabilidadDA)
print("P(D|B) =                 ",probabilidadDB)
print("P(D|C) =                 ",probabilidadDC)
                    ##
                    ##
                    ##
#3. ¿Hay relaciones de dependencia o independencia entre las características? ¿De qué tipo?
# Dado que la independencia estadistica se define, según a teoria brindada y estudiada, como
# eventos llamados estadísticamente independientes si la probabilidad de ocurrencia de un evento
#no es afectada por la ocurrencia del otro evento dado esto cuando se calcule * P(A | B) = P(A)
# y P(B | A) = P(B).

# Considerando que se pregunta por la dependencia o independencia de una característica respecto a las demás,
# se toma en cuenta la aclaración realizada por el profesor en donde menciona que:
# "Lo primero que se puede hacer es analizar independencia entre pares.
# Algunos pueden ser dependientes y otros independientes. Con solo que haya alguno dependiente
# ya no hay que analizar más porque la independencia como conjunto implica independencia entre todos".
# Procedemos a verificar para cada combinación, entonces se realizará un loop de verificacion.
# Se crea un array donde se almacenan las probabilidades de ocurrencia de cada caracteristica.
ResultadoOcurrencia = [probabilidadA,probabilidadB, probabilidadC, probabilidadD]
ProbabibilidadDebidoaOtraA = [probabilidadAB, probabilidadAC,probabilidadAD]
ProbabibilidadDebidoaOtraB = [probabilidadBA, probabilidadBC,probabilidadBD]
ProbabibilidadDebidoaOtraC = [probabilidadCA, probabilidadCB,probabilidadCD]
ProbabibilidadDebidoaOtraD = [probabilidadDA, probabilidadDB,probabilidadDC]
#Realizo un contador para que sume si hay dependencia o no entre carcateristicas.
dependeciaA =0
dependeciaB =0
dependeciaC =0
dependeciaD =0
# Dado lo comentado por el profesor con el fin de poder verificar si son dependientes o no, se puede ya sea tomar los valores
# a como son calculados o considerar un grado de incertidumbre. Se sigue la siguiente lógica para definir mi propio de rango de
# incertidumbre. Con una muestra de 500 tomas de datos si considero que en todos los casos se da dicha característica un 5% de
# estos datos equivalen a 25 tomas. Si considero un  muestra_total*0.5% donde la muestra total de 499 son ~ 2.5 tomas lo que por
# su cualidad se consideran dos muestras. Me parece adecuado considerar que si en un rango de 500 muestra se tomen 2 muestras como
# incertidumbre, esto me facilita un criterio para evaluar que tan cercano está una probabilidad de ocurrencia respecto a la
# probabilidad de una caracteristica dada la otra.

# Es muy importante tener en cuenta que el nivel de incertidumbre aceptado siguiendo la lógica anterior va a variar conforme
# varie la cantidad de la toma de datos.

# Utilizando la analogia anterior ...
print("\nSe analiza independencia y dependencia de una probabilidad de que suceda una caracteristica dada la otra con un 0.005 de incertidumbre respecto a la probabilidad de ocurrencia \n")
#Revisando para A
print("\nResultados de dependencia siguiendo el orden: probabilidadAB, probabilidadAC, probabilidadAD")
for combisA  in ProbabibilidadDebidoaOtraA: #AB AC AD
    if abs(ResultadoOcurrencia[0] - combisA) <= 0.005: # A - AB <= 0.005
        dependeciaA = dependeciaA +1
        if dependeciaA != 0:
            print("La relación ", combisA," es de INDEPENDENCIA")
    else:
        print("La relación ",combisA," es de DEPENDENCIA")

print("\nResultados de dependencia siguiendo el orden: probabilidadBA, probabilidadBC, probabilidadBD")
#Revisando para B
for combisB in ProbabibilidadDebidoaOtraB:
    if abs(ResultadoOcurrencia[1] - combisB) <= 0.005:
        dependeciaB = dependeciaB +1
        if dependeciaB != 0:
            print("La relación ", combisB," es de INDEPENDENCIA")
    else:
        print("La relación ",combisB," es de DEPENDENCIA")

#Revisando para C
print("\nResultados de dependencia siguiendo el orden: probabilidadCA, probabilidadCB, probabilidadCD")
for combisC in ProbabibilidadDebidoaOtraC:
    if abs(ResultadoOcurrencia[2] - combisC) <= 0.005:
        dependeciaC = dependeciaC +1
        if dependeciaC != 0:
            print("La relación ", combisC," es de INDEPENDENCIA")
    else:
        print("La relación ",combisC," es de DEPENDENCIA")

#Revisando para D
print("\nResultados de dependecia siguiendo el orden: probabilidadDA, probabilidadDB, probabilidadDC")
for combisD in ProbabibilidadDebidoaOtraD:
    if abs(ResultadoOcurrencia[3] - combisD) <= 0.005:
        dependeciaD = dependeciaD +1
        if dependeciaD != 0:
            print("La relación ", combisD," es de INDEPENDENCIA")
    else:
        print("La relación ",combisD," es de DEPENDENCIA")
print("\nConsiderando la teoría analizada, si existe dependencia entre pares no existe independencia como conjunto ya que la independencia como conjunto implica independencia entre todos")


                    ##
                    ##
                    ##
#4. Si hay una característica tipo D, ¿cuál es la probabilidad de que también tenga la característica A?
# Considerando que son eventos independientes, sabemos que la probabilidad conjunta para eventos independientes
# se calcula como P(A | D) lo cual ya habíamos calculado para la sección 2.
#Sabemos que:
print("\nLa probabilidad de que si está la característica D tambien posea A es:\nP(A|D)=                  ", probabilidadAD)
