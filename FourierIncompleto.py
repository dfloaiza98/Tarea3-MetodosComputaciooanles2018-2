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

#Ploteo de la transformada de Fourier de los datos signal.dat
xdata = signaldata[:,0]
DFTdatos = ordinary_dft(signaldata[:,1])
frequ = fftfreq(len(signaldata),xdata[1]-xdata[0])

plt.figure()
plt.plot(frequ,abs(DFTdatos), color = "blue")
plt.title("Discrete Fourier Transform of signal.dat")
plt.xlabel("Frequency(Hz)")
plt.ylabel("Amplitude")
plt.xlim([-700,700])
plt.savefig("LoaizaDaniel_TF.pdf")


#Mensaje indicando cuales son las principales frecuencias.
print "Las principales frecuencias son: "
print frequ[(DFTdatos)>100]

#Filtro pasa bandas con frecuencia de corte = 1000 Hz.	

frecdecorte=1000
DFTdatos[np.abs(frequ)>frecdecorte]=0
inverseTrans=ifft(DFTdatos)
plt.figure()
plt.plot(signaldata[:,0],np.real(inverseTrans))
plt.title("Filter of signal.dat")
plt.ylabel("Real signal")
plt.xlabel("Tiempo")
#plt.savefig("LoaizaDaniel_filtrada.pdf")








