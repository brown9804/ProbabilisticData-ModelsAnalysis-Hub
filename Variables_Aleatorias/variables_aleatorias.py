# Belinda Brown Ramírez
# Mayo, 2020
# timna.brown@ucr.ac.cr

#               Variables aleatorias
# La variable aleatoria es una función, se caracteriza por ser determinista
#

#Datos a partir de la base llamada datos.cvs

####   ****************         Algoritmo            ****************   ####

#******************************************************
#               IMPORTANDO PAQUETES
#******************************************************
from __future__ import division
import csv
from pylab import *
import matplotlib.pyplot as plt
from sklearn import *
from sklearn.preprocessing import PolynomialFeatures
from numpy import *
import numpy as np
import math
from collections import OrderedDict
import decimal
import scipy.stats as stats
import pandas as pd
import matplotlib.mlab as mlab
from scipy.stats import norm
from scipy.stats import rayleigh

#******************************************************
#               DEFINICIONES
#******************************************************

####                MEDIDAS ARITMETICAS NECESARIAS
def media_arit_lista(lista):
	n = len(lista) + 1
	sumatoria = 0
	for i in lista:
		sumatoria = sumatoria + float(i)
	return sumatoria/n

def varianza_lista(lista):
	n = len(lista) + 1
	sum_var = 0
	for j in lista:
		sum_var = sum_var + (media_arit_lista(lista)-float(j))**2
	return sum_var/n

def desvia_estan_lista(lista):
	desvi = varianza_lista(lista)**(1/2)
	return desvi

def curtosis(lista, media, varianza):
	n = len(lista) + 1
	funcion = 0
	k0 = 0
	for k in lista:
		funcion = (float(k)- float(media))/float(varianza)
		k0 = k0 + float(funcion)**4
	kx = k0 - 3
	return kx

def intervalo(data):
	inter = []
	for k in data:
		redondeado = round(float(k))
		# Rango de 12 a 54
		if(12<=redondeado) and (redondeado<=54):
			inter.append(float(k))
	return inter

# Obteniendo la informacion del archivo .csv
with open("datos.csv", "r") as csv_file:
	# Leyendo cada celda y separandola con coma para poder interpretar los datos
	csv_reader = csv.reader(csv_file, delimiter=',')
	# Se salta la primera linea del CSV
	next(csv_reader)
	# Arerglo para guardar los datos aleatorios
	data = []
	# Recorre todas las filas dentro del archivo cvs
	for filas_completas_data in csv_reader:
		# Se guardan los datos en un arreglo
		data.append(float(filas_completas_data[0]))

	#*******************************************************************
	###            CALCULO DE LOS 4 PRIMEROS MOMENTOS
	#*******************************************************************
	# Permiten resumir el comportamiento de las variables de manera general
	# Se requiere de la media aritmetica para calcular los momentos de
	# Rayleigh, entonces:
	mu, sigma = stats.rayleigh.fit(data)
	# print(mu)
	# print(sigma)
	desv = stats.rayleigh (mu, sigma)
	media_pandas, var_pandas, inclinacion_pandas, curtosis_pandas = desv.stats(moments='mvsk')
	print("La media obtenida desde pandas es de:              ", media_pandas)
	print("La varianza obtenida desde pandas es de:               ", var_pandas)
	print("El sesgo obtenido desde pandas es de:					", inclinacion_pandas)
	print("La curtosis obtenida desde pandas es de:                  ", curtosis_pandas)

	# # Los 4 momentos en funciones creadas se describen como:
	# 1. Varianza medida de la dispersión de la función al rededor del promedio
	media = media_arit_lista(data)
	print("\n\n\n\nLa media de la definición creada:                  ", media)
	varianza = varianza_lista(data)
	print("La varianza de la definición creada:                           ",varianza)
	# # 2. Desviación estándar es el cuadrado de la varianza
	desviacion_std = desvia_estan_lista(data)
	print("El valor de la desviación estándar de la definición creada:     ", desviacion_std)
	# # 3. Sesgo (Inclinación) refiere a la tendencia que tiene una descripcion completa
	# # de la variable aleatoria. Si es cero la  pdf es simetrica, negativa tiende a la izquierda
	# # y positivo tiende a la derecha
	funcion = 0
	sx = 0
	for k in data:
		funcion = (float(k)- float(media))/float(varianza)
		f4 = float(funcion)*float(funcion)*float(funcion)
		sx = sx + float(f4)
	print("El sesgo de la definición creada:                  ", sx)
	# # 4. Curtosis (Medidad de abultamiento)
	# # Se denomina como kx, si kx < 0 es achatada es decir como si tanta cima
	# # Si k>0 es prominente como si fuese una montaña, sería empinada
	curtosis_resp = curtosis(data, media, varianza)
	print("Curtosis de la definición creada:                         ", curtosis_resp)

	#******************************************************
	###                  HISTOGRAMA de DATA
	#******************************************************
	##Ahora con la información almacenada en el arreglo "data"
	###se procede a crear el histograma
	histograma = plt.hist(data,30, density=True)
	plt.savefig('Histograma de data ')
	# #                   Limpia el area de graficacion
	plt.cla()
	#******************************************************
	###                     CURVA DE MEJOR AJUSTE A LOS DATOS
	#******************************************************

	N = len(data) +1
	escala = media_pandas/np.sqrt(np.pi/2)
	V_norm_hist = escala * np.sqrt( -2* np.log (np.random.uniform(0, 1, N)))
	fig, ax = plt.subplots(1, 1)
	num_bins = 30
	_binvalues, bins, _patches = plt.hist(V_norm_hist, bins=num_bins, density=False, rwidth=1, ec='blue', label='Histograma')
	x = np.linspace(bins[0], bins[-1], 120)
	binwidth = (bins[-1] - bins[0]) / num_bins
	escala = V_norm_hist.mean()/np.sqrt(np.pi/2)
	plt.plot(x, rayleigh(loc=0, scale=escala).pdf(x)*len(V_norm_hist)*binwidth, lw=5, alpha=0.6, label='Rayleigh pdf)')
	plt.legend()
	plt.savefig('Curva de mejor ajuste')
	# #                   Limpia el area de graficacion
	plt.cla()
	#*******************************************************************
	###             ENCONTRAR LA PROBABILIDAD EN EL INTERVALO [a,b]
	###             Y CONTRARESTARLO CON LA FRECUENCIA RELATIVA
	#*******************************************************************

	# Como mi carnet es B61254, de acuerdo a las instrucciones se toma como
	# a = 12
	# b = 54
	#### Calculando el intervalo y la probabilidad de esta
	# Se ordena la función de menor a mayor para acotar este intervalo y calcular su probabilidad
	# Guardo los valores entre 12 y 54
	numeros1254 = 0
	intervalo1254 = intervalo(data)
	# print(intervalo1254)
	for i in range(N):
		# print(i)
		for j in intervalo1254:
			numeros1254 = numeros1254 + j
	# Ya tengo los datos que pertenecen dentro del intervalo1254
	# 	# Para la frecuencia relativa
	# # Lo que se hace es dividir estos valores entre la cantidad total de datos
	# # Esta cantidad estaba almacenada en la variable N
	frecuencia_relativa1254 = numeros1254/N
	print("\n \nLa frecuencia relativa perteneciente al intervalo [12, 54] es de:	", frecuencia_relativa1254)
	# #	#  Calculando la probabilidad
	probabilidad = desv.cdf(54) - desv.cdf(12)
	print( 'La probibilidad obtenida mediante las funciones importadas para este rango es de: ', probabilidad)
	#*******************************************************************
	###            TRANSFORMACIONES
	#*******************************************************************
	## Se considera que los datos del arhicvo csv son X
	## Se debe realizar Y = sqrt(X) que es la transformacion.
	## Porteriormente se grafica su histrograma
	# Entonces para todos los valores en la data
	sqrt_x = 0
	Y_trasnfor= []
	for values in data:
		sqrt_x = float(values)**(1/2)
		Y_trasnfor.append(sqrt_x)
	#******************************************************
	###                  HISTOGRAMA de TRANSFORMACION
	#******************************************************
	##Ahora con la información almacenada en el arreglo "data"
	###se procede a crear el histograma
	histograma = plt.hist(Y_trasnfor,30)
	plt.savefig('Histograma transformacion')
	# #                   Limpia el area de graficacion
	plt.cla()

	#******************************************************
	# ###                 FUNCION DE DENSIDAD de la TRANSFORMACION
	# #******************************************************
	media_y = media_arit_lista(Y_trasnfor)
	print("La media de la transformación:				", media_y)
	desviacion_y = desvia_estan_lista(Y_trasnfor)
	print("La desviación de la transformación", desviacion_y)
	distribucion_y = norm(loc=media_y, scale=desviacion_y)
	x_transf = np.linspace(distribucion_y.ppf(0.001),distribucion_y.ppf(0.999), 120)
	plt.hist(Y_trasnfor,density=True, label='Transformacion')
	plt.plot(x_transf, distribucion_y.pdf(x_transf), 'r-', label='PDF teorico')
	plt.legend()
	plt.savefig('Funcion de densidad de la transformacion')
