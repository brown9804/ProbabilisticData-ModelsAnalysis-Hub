#           Variables Múltiples 
----------
Modelos Probabilísticos de Señales y Sistemas

Universidad de Costa Rica

Belinda Brown, B61254

Junio, 2020
----------

## Correr el programa
Con el fin de probar el programa, se requieren revisar los paths contenidos en el main.py el cual se encuentra dentro de la carpeta de "src" ya que estos paths están dirigidos a mi máquina. Después de realizar esto se cuenta con un makefile el cual permite probar el algoritmo y limpiar la carpeta de "results" en donde se encuentran los resultados. Se siguen los siguientes comandos.

Para analizar todo lo requerido se debe ingresar:

**1. <path_donde_se_encuentra_el_folder>$ make analize**
 
Para borrar los resultados obtenidos se debe digitar:

**2. <path_donde_se_encuentra_el_folder>$ make clean**

## Paquetes importados
~~~~
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
# import csv
import pandas as pd
from collections import OrderedDict
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
from mpl_toolkits.mplot3d import axes3d
from numpy import *
import numpy as np
from matplotlib import cm
import scipy.stats as stats
from scipy.optimize import curve_fit
~~~~

## Definciones 
~~~~
def distribucion_normal(va, mu, sigma):
	dist_normal = 1/(np.sqrt(2*np.pi*sigma**2)) * np.exp(-(va-mu)**2/(2*sigma**2))
	return dist_normal

def densidad_conjunta(va0,va1,mu0,sigma0,mu1,sigma1):
	val_conjunto = 1/((np.sqrt(2*np.pi*sigma0**2)) * np.exp(-(va0-mu0)**2/(2*sigma0**2)) * (1/(np.sqrt(2*np.pi*sigma1**2)) * np.exp(-(va1-mu1)**2/(2*sigma1**2))))
	return val_conjunto


def ajuste_curva(marginal, par1, par2, distri_norm, graph_label_dis, distri_x_name_img, func_graph_label, function_va_img):
	va = np.linspace(par1,par2,len(marginal))
	plt.bar(va, marginal, label= graph_label_dis)
	plt.legend()
	plt.savefig("/Users/belindabrown/Desktop/VA_multiples/results/" + distri_x_name_img + ".png")
	parametros_va, _ = curve_fit(distri_norm, va, marginal)
	mu, sigma = parametros_va[0], parametros_va[1]
	print("\n\nMu " + distri_x_name_img + " =		", mu)
	print("Sigma " + distri_x_name_img + "  = 		", sigma)
	va_function = stats.norm(mu,sigma)
	curva_ajustada = np.linspace(va_function.ppf(0.01), va_function.ppf(0.99), 100)
	plt.plot(curva_ajustada,va_function.pdf(curva_ajustada),label=func_graph_label)
	plt.legend()
	plt.savefig("/Users/belindabrown/Desktop/VA_multiples/results/" + function_va_img+".png")
	# #                   Limpia el area de graficacion
	plt.cla()
	return curva_ajustada, mu, sigma

def esperado(marginal,lim_inferior,lim_superior, de_quien_v_esperado):
	dominio = []
	esperado_marginal = 0
	for k in range (5, lim_superior +1):
		dominio.append(k)
	dominio = list(OrderedDict.fromkeys(dominio))
	print("\n\nEl dominio es de:		", dominio)
	for i in range (0,len(marginal)):
	    esperado_marginal = esperado_marginal + dominio[i]*marginal[i]
	print("\n" +de_quien_v_esperado +" tiene un valor esperado de:	", esperado_marginal)
	return esperado_marginal

def grafica_en2d(mu_va, sigma_va, par1_modelo, nombre2d):
	va_funcion_distri = stats.norm(mu_va,sigma_va)
	curve = np.linspace(va_funcion_distri.ppf(0.01), va_funcion_distri.ppf(0.99), par1_modelo)
	plt.plot(curve,va_funcion_distri.pdf(curve),label=nombre2d)
	plt.legend()
	plt.savefig("/Users/belindabrown/Desktop/VA_multiples/results/" + nombre2d+".png")
	# #                   Limpia el area de graficacion
	plt.cla()
	return

def grafica_en3d(VA0_modelo, VA1_modelo, VA0, VA1, nombre):
	Z = []
	for i in VA0:
		XY = []
		for j in VA1:
			XY.append(i*j)
		Z.append(XY)
	fig = plt.figure()
	eje_x= plt.axes(projection='3d')
	VA0,VA1 = np.meshgrid(VA0_modelo,VA1_modelo)
	eje_x.plot_surface(VA0,VA1,np.array(Z),cmap=cm.coolwarm)
	plt.savefig("/Users/belindabrown/Desktop/VA_multiples/results/" + nombre+".png")
	return
~~~~

## Importanción de los valores en las bases de datos
~~~~
data = pd.read_csv("/Users/belindabrown/Desktop/VA_multiples/data_base/xy.csv", index_col=0)
data_xyp = pd.read_csv("/Users/belindabrown/Desktop/VA_multiples/data_base/xyp.cs
~~~~

## Curva de mejor ajuste para las funciones de densidad marginales de X & Y
Apartir de los datos en las bases .csv,se encuentra la mejor curva de ajuste (modelo probabilístico) para las funciones de densidad marginales de X y Y. 
~~~~
# Se requieren los valores marginales tanto de x como de y
# Columna con la sumatoria de todas las columnas es la probabilidad marginal de X
marg_value_x = [n for n in data.sum(axis=1, numeric_only=True)]
# Fila con la sumatoria de todas las filas es la probabilidad marginal de Y
marg_value_y = [n for n in data.sum(axis=0, numeric_only=True)]
print("\nValor marginal de X: ", marg_value_x)
print("\nValor marginal de Y: ", marg_value_y)
x_curva_modelo, x_mu, x_sigma = ajuste_curva(marg_value_x, 5, 15, distribucion_normal, "Datos que pertenencen a X","Datos_de_X", "Modelos de X(x)", "Modelado_X(x)")
y_curva_modelo, y_mu, y_sigma = ajuste_curva(marg_value_y, 5, 25, distribucion_normal, "Datos que pertenencen a Y","Datos_de_Y", "Modelos de Y(y)", "Modelado_Y(y)")
~~~~

### Para X
![image] (results/Datos_de_X.png)
![image] (results/Modelado_X(x).png)

### Para Y
![image] (results/Datos_de_Y.png)
![image] (results/Modelado_Y(y).png)


