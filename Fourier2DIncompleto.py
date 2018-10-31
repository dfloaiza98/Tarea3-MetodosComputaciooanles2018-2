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



for i in range(np.shape(shift)[0]):
	for j in range(np.shape(shift)[1]):
		if (shift[i][j]>2300 and shift[i][j]<29000 ):
			shift[i][j] = 0
		else:
			shift[i][j] = shift[i][j]
		


