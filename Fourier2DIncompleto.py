#Punto 4, tarea3 de Metodos computacionales 2018-2. Daniel Loaiza, cod=201615258.
#Importacion de librerias necesarias.

import matplotlib.pylab as plt
import numpy as np
from scipy import fftpack
from matplotlib.colors import LogNorm



#Almacenamiento de la imagen en un arreglo.
image= plt.imread("arbol.png").astype(float)

#Tranformada de Fourier en 2D para la imagen arbol.png
transImage= fftpack.fft2(image)


plt.figure()
plt.imshow(np.abs(transImage), cmap="gray")
plt.colorbar()
#plt.savefig("LoaizaDaniel_FT2D.pdf")



#Pruebas de como modificar fft para eliminar el ruido periodico en la imagen arbol.png


# Define the fraction of coefficients (in each direction) we keep
fraction = 0.084
# Copia de la transformada para no alterar la transformada original.
copiaTrans = np.copy(transImage)


filas = copiaTrans.shape[0]
columnas = copiaTrans.shape[1]

copiaTrans[int(filas*fraction):int(filas*(1-fraction))] = 0

copiaTrans[:, int(columnas*fraction):int(columnas*(1-fraction))] = 0


