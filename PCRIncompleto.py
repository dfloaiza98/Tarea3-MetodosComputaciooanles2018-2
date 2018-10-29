#Punto de PCR y PCA, tarea 3 de metodos computacionales de Daniel Loaiza. 201815258

#Importacion de librerias esenciales.
import numpy as np
import matplotlib.pylab as plt

#Almacenamiento de los datos del archivo WDBC.dat

dataPCA = np.genfromtxt("WDBC.dat",None,delimiter="\n")



#Creacion del vector de datos para saber si es Maligno o Benigno el diagnostico.
vectorMoB = np.zeros(len(dataPCA))
