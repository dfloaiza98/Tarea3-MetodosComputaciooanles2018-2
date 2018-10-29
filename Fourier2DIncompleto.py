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
