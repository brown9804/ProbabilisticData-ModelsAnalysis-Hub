##--------------------------------Main file------------------------------------
##
##                          Copyright (C) 2020
##             by Belinda Brown Ramírez (belindabrownr04@gmail.com)
##					Based on course material
##			       Julio, 2020
##		          timna.brown@ucr.ac.cr
##-----------------------------------------------------------------------------

# Se considera un servicio, en donde la tasa de clientes es de 2:

#			a = clientes/minuto

# Entonces se quiere mantener una cola de no más de 5 personas en el 95% del
# tiempo. Para los servidores hay una cantidad de s en donde la tasa de cada uno
# de atención (es lo mismo que tiempo promedio de atención) es de b donde la base
# de b es de 1. Tanto s como b se deben adecuar para cumplir el porcentaje dado
# a partir de un presupuesto limitado de 100 markovs. Donde en este caso los
# markov es la moneda.

# Se inicia con un servidor, por cada servidor extra son 30 markovs. Ahora con
# respecto a la licencia se tiene que una licencia la cual duplica la cantidad de
# b para cda servidor cuesta 20 markovs.


####   ****************         Algoritmo            ****************   ####

#******************************************************
#               IMPORTANDO PAQUETES
#******************************************************
import csv
import pandas as pd
import matplotlib.pyplot as plt
from numpy import *
from numpy import genfromtxt
import numpy as np
from scipy import signal
from scipy import integrate
import scipy.stats as stats
from matplotlib import cm

#******************************************************
#		DEFINICIONES
#******************************************************
def viabilidad(N_clientes, clientes_x_s, servidores_x_s, clientes_x_fila):
	# Parámetro de llegada (clientes/segundos)
	lam = clientes_x_s/60
	# Parámetro de servicio (servicios/segundos)
	nu = servidores_x_s/60
	# Distribución de los tiempos de llegada entre cada cliente
	X = stats.expon(scale = 1/lam)
	# Distribución de los tiempos de servicio a cada cliente
	Y = stats.expon(scale = 1/nu)
	# Intervalos entre llegadas (segundos desde último cliente)
	t_inte = np.ceil(X.rvs(N_clientes)).astype('int')
	# Tiempos de las llegadas (segundos desde el inicio)
	t_lleg = [t_inte[0]]
	for i in range(1, len(t_inte)):
	    siguiente = t_lleg[i-1] + t_inte[i]
	    t_lleg.append(siguiente)
	# Tiempos de servicio (segundos desde inicio de servicio)
	t_serv = np.ceil(Y.rvs(N_clientes)).astype('int')
	# Inicialización del tiempo de inicio y fin de atención
	inicio = t_lleg[0]          # primera llegada
	fin = inicio + t_serv[0]    # primera salida
	# Tiempos en que recibe atención cada i-ésimo cliente (!= que llega)
	t_aten = [inicio]
	for i in range(1, N_clientes):
	    inicio = np.max((t_lleg[i], fin))
	    fin = inicio + t_serv[i]
	    t_aten.append(inicio)
	# Inicialización del vector temporal para registrar eventos
	t = np.zeros(t_aten[-1] + t_serv[-1] + 1)
	# Asignación de eventos de llegada (+1) y salida (-1) de clientes
	for c in range(N_clientes):
	    i = t_lleg[c]
	    t[i] += 1
	    j = t_aten[c] + t_serv[c]
	    t[j] -= 1
	# Umbral de P o más personas en sistema (hay P - 1 en fila)
	P = clientes_x_fila
	# Instantes (segundos) de tiempo con P o más solicitudes en sistema
	frecuencia = 0
	# Proceso aleatorio (estados n = {0, 1, 2...})
	Xt = np.zeros(t.shape)
	# Inicialización de estado n
	n = 0
	# Recorrido del vector temporal y conteo de clientes (estado n)
	for i, c in enumerate(t):
	    n += c # sumar (+1) o restar (-1) al estado
	    Xt[i] = n
	    if Xt[i] >= P:
	        frecuencia += 1
	# Fracción de tiempo con P o más solicitudes en sistema
	fraccion = frecuencia / len(t)
	return t, lam, nu, fraccion, P, Xt

def graph_clients_x_se(lengenda, y_label, x_label,tvalor, pvalor, Xt_valor):
	# Gráfica de X(t) (estados del sistema)
	plt.figure()
	plt.plot(Xt_valor)
	plt.plot(range(len(tvalor)), (pvalor-1)*np.ones(tvalor.shape))
	plt.legend(lengenda)
	plt.ylabel(y_label)
	plt.xlabel(x_label)
	plt.show()
	return

#******************************************************
#		SIMULACION DE LA PROPUESTA DE
# 		COMBINACION DE S & B PARA PRESUPUESTO
#******************************************************
# Parámetros viabilidad(N_clientes, clientes_x_s, servidores_x_s, clientes_x_fila)
t_1, lam_1, nu_1, fraccion_1, P_1, Xt_1= viabilidad(10000,2, 4, 5)

print('Parámetro de clientes por segundo --> lambda = ', str(lam_1*60))
print('Parámetro de servicio --> nu = ', str(nu_1*60))
print('Tiempo con más de {} solicitudes en fila:'.format(P_1-2))
print('\t {:0.2f}%'.format(100*fraccion_1))
if fraccion_1 <= 0.05:
    print('\t Sí cumple con la especificación.')
else:
    print('\t No cumple con la especificación.')
print('Simulación es equivalente a {:0.2f} horas.'.format(len(t_1)/3600))

#************* Visualización ********************
graph_clients_x_se(('$X(t) = n$', '$L_q = $' + str(P_1-2)),'Clientes en el sistema, n', 'Tiempo, t / segundos', t_1, P_1, Xt_1)
