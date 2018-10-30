#Punto3 de la tarea3 de metodos computacionales,2018-2. Daniel Loaiza, cod=201615258
#Librerias esenciales
from scipy import interpolate
import numpy as np
import matplotlib.pylab as plt
import cmath
import math
from scipy.fftpack import ifft, fftfreq


#Almacenamiento de los datos signal.dat e incompletos.dat
signaldata =np.genfromtxt("signal.dat",delimiter=",")
incompletedata=np.genfromtxt("incompletos.dat",delimiter=",")


#Ploteo de los datos 
plt.figure()
plt.plot(signaldata[:,0],signaldata[:,1],color = "red",label = "data of signal.dat")
plt.title("Signal.dat")
plt.xlabel("Time")
plt.ylabel("Signal recorded")
plt.legend(loc='lower left')
plt.savefig("LoaizaDaniel_signal.pdf")

#Implementacion propia de la Transformada de Fourier Discreta. 

def ordinary_dft(x):
    trX=np.zeros(len(x))
    N=len(x)
    for n in range(N):
        s=0
        for k in range(N):
            s+=x[k]*cmath.exp(-2*math.pi*1j*n*k/N)
        trX[n]=(s)
    return trX





