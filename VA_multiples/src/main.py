# Belinda Brown Ramírez
# Junio, 2020
# timna.brown@ucr.ac.cr

#            Variables aleatorias múltiples
# Se consideran dos bases de datos las cuales contienen los descrito
# a continuación:
# 1. ****** Registro de la frecuencia relativa de dos variables aleatorias
# conjuntas en forma de tabla:  xy.csv
# 2. ****** Pares (x, y) y su probabilidad asociada: xyp.csv
# Recordando que variable aleatoria es una función determinista.

####   ****************         Algoritmo            ****************   ####

#******************************************************
#               IMPORTANDO PAQUETES
#******************************************************
# Es importante considerar que notas son necesarias pero si
# fueron usadas durante el desarrollo de la tarea por diversas
# razones por lo cual se mantiene dentro del algortimo en forma
# comentario.
# from __future__ import division
# from pylab import *
# from sklearn import *
# from sklearn.preprocessing import PolynomialFeatures
# import math
# import decimal
# import pandas as pd
# from scipy.stats import norm
# from scipy.stats import rayleigh
import csv
from collections import OrderedDict
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
from numpy import *
import numpy as np
import scipy.stats as stats
from scipy.optimize import curve_fit



#******************************************************
#               DEFINICIONES
#******************************************************

# (25 %) A partir de los datos, encontrar la mejor curva
# de ajuste (modelo probabilístico) para las funciones de
# densidad marginales de X y Y.
#(25 %) Asumir independencia de X y Y. Analíticamente,
# ¿cuál es entonces la expresión de la función de densidad
#  conjunta que modela los datos?
# (25 %) Hallar los valores de correlación, covarianza y
# coeficiente de correlación (Pearson) para los datos y
# explicar su significado.
# (25 %) Graficar las funciones de densidad marginales (2D),
#  la función de densidad conjunta (3D).
####



# Obteniendo la informacion del archivo .csv
with open("./data_base/xp.csv", "r") as csv_file:
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
