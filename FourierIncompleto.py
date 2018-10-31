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
plt.savefig("LoaizaDaniel_filtrada.pdf")

#Explicacion de porque no se puede hacer dft de los datos incompletos.dat

print "La razon por la cual no se puede hacer la transformada de fourier discreta de incompletos.dat es porque este archivo tiene muy pocos puntos."


#Interpolacion cuadratica y cubica de incompletos.dat con 512 puntos.

quadratic = interpolate.interp1d(incompletedata[:,0],incompletedata[:,1],kind = "quadratic")
cubic = interpolate.interp1d(incompletedata[:,0],incompletedata[:,1],kind = "cubic")
incompletedataX=incompletedata[:,0]
Xaxis = np.linspace(incompletedataX[0],incompletedataX[-1],512)
dataInterpolquad = quadratic(Xaxis)
dataInterpolcub = cubic(Xaxis)

#Variables que guardan la transformada discreta de fourier de los datos originales e interpolados del archivo incompletos.dat
DFTnormales=ordinary_dft(incompletedata[:,1])
DFTinterquad=ordinary_dft(dataInterpolquad)
DFTintercub=ordinary_dft(dataInterpolcub)
dt= (incompletedataX[1]-incompletedataX[0])
freqOriginalIncomplete = fftfreq(len(incompletedata),dt)
freqInterpol = fftfreq(len(Xaxis),dt)



#Subplots de la transformada discreta de fourier de los datos originales y de las interpolaciones cubica y cuadratica.
plt.figure()
plt.subplot(131)
plt.plot(freqOriginalIncomplete,abs(DFTnormales),color="Yellow",label="Original")
plt.legend(loc='upper left')
plt.ylabel("Amplitude")
plt.xlabel("Freq.(Hz)")
plt.subplot(132)
plt.plot(freqInterpol,abs(DFTinterquad),color="blue",label="Inter.Quad")
plt.xlim(-800,800)
plt.legend(loc='upper left')
plt.ylabel("Amplitude")
plt.xlabel("Freq.(Hz)")
plt.subplot(133)
plt.plot(freqInterpol,abs(DFTintercub),color = "pink",label="Inter.Cubic")
plt.legend(loc='upper left')
plt.ylabel("Amplitude")
plt.xlabel("Freq.(Hz)")
plt.xlim(-800,800)
plt.savefig("LoaizaDaniel_TF_interpola.pdf")

#Imprima un mensaje donde describa las diferencias encontradas entre la transformada de Fourier de la senal original y las de las interpolaciones.


print "Lo primero que yo noto es que los picos de las interpoladas son mucho mas altos(mas magnitud) que los picos de la senal original del archivo incompletos.dat. Tambien las graficas interpoladas son mucho mas 'suaves'. Los valores horizontales tambien son una diferencia notable dado que la grafica de los datos originales alcanza valores horizontales varios ordenes de magnitud mas grande que las dos graficas interpoladas. Por ultimo, como la interpolacion brinda una grafica con mas puntos, ahora en las interpolaciones pueden verse graficas con cierto patron y en los datos originales no."


#Filtro pasabajos para fc=1000 y para fc=500.

## Filtro fc = 1000Hz
fc1=1000
DFTnormales[abs(freqOriginalIncomplete)>fc1]=0
OriginalSignalfc1=ifft(DFTnormales)
DFTinterquad[abs(freqInterpol)>fc1]=0
realQuadfc1=ifft(DFTinterquad)
DFTintercub[abs(freqInterpol)>fc1]=0
realCubfc1=ifft(DFTintercub)

#Filtro fc = 500Hz
fc2=500
DFTnormales[abs(freqOriginalIncomplete)>fc2]=0
OriginalSignalfc2=ifft(DFTnormales)
DFTinterquad[abs(freqInterpol)>fc2]=0
realQuadfc2=ifft(DFTinterquad)
DFTintercub[abs(freqInterpol)>fc2]=0
realCubfc2=ifft(DFTintercub)

#Subplots para cada senal real, unos para una frecuencia de corte de 1000Hz y otros para la frecuencia de corte de 500Hz.
plt.figure()
plt.subplot(321)
plt.plot(incompletedata[:,0],np.real(OriginalSignalfc1),color="Yellow",label="Original fc=1000")
plt.legend(loc='upper left')
plt.ylabel("Real Amplitude")
plt.xlabel("Time")
plt.subplot(322)
plt.plot(incompletedata[:,0],np.real(OriginalSignalfc2),color="yellow",label="Original fc=500")
plt.legend(loc='upper left')
plt.ylabel("Real Amplitude")
plt.xlabel("Time")
plt.subplot(323)
plt.plot(Xaxis,np.real(realQuadfc1),color = "blue",label="Inter.quad fc=1000")
plt.legend(loc='upper left')
plt.ylabel("Amplitude")
plt.xlabel("Time")
plt.subplot(324)
plt.plot(Xaxis,np.real(realQuadfc2),color = "blue",label="Inter.quad fc=500")
plt.legend(loc='upper left')
plt.ylabel("Real Amplitude")
plt.xlabel("Time")
plt.subplot(325)
plt.plot(Xaxis,np.real(realCubfc1),color = "red",label="Inter.cub fc=1000")
plt.legend(loc='upper left')
plt.ylabel("Real Amplitude")
plt.xlabel("Time")
plt.subplot(326)
plt.plot(Xaxis,np.real(realCubfc2),color = "red",label="Inter.cub fc=500")
plt.legend(loc='upper left')
plt.ylabel("Real Amplitude")
plt.xlabel("Time")
plt.savefig("LoaizaDaniel_2Filtros.pdf")









