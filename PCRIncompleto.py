#Punto de PCR y PCA, tarea 3 de metodos computacionales de Daniel Loaiza. 201815258

#Importacion de librerias esenciales.
import numpy as np
import matplotlib.pylab as plt

#Almacenamiento de los datos del archivo WDBC.dat

dataPCA = np.genfromtxt("WDBC.dat",None,delimiter="\n")



#Creacion del vector de datos para saber si es Maligno o Benigno el diagnostico.
vectorMoB = np.zeros(len(dataPCA))

#Creacion del arreglo que contiene los datos tomados durante la prueba.
pruebas = np.zeros([len(dataPCA),30])
for i in range(len(dataPCA)):
    fila = (dataPCA[i].decode('UTF-8')).split(",")
    
    #Asignacion de 1 o 2 para los datos de diagnostico, 1 si es maligno o 2 si es benigno.
    if fila[1]=='M':
        vectorMoB[i]=1
    elif fila[1]=='B':
        vectorMoB[i]=2
    
    #Clasificacion datos pruebas
    for j in range(30):
        pruebas[i][j]=(datosFila)[j+2]

#Creacion de la matriz que contiene los datos del archivo WDBC.dat
datamatrix = np.transpose(pruebas)


#Funcion para estandarizar el set de datos. Esta funcion resta el promedio de los sed de datos y posteriormente divide el set de datos en la desviacion estandar. Esto es necesario siempre que se vaya a hacer PCA.
def estandariza(data):
    for j in range (30):
        fila=data[j]
        m=np.mean(fila)
        st=np.std(fila)
        for i in range(569):
            data[j][i]=(data[j][i]-m)/st
    return data


#Funcion que calcula la matriz de covarianza.
def cov_matrix(data):
    cov=np.zeros((30,30))
    for i in range (30):
        for j in range (30):
            s=0
            for k in range (569):
                s+=data[i][k]*data[j][k]
            s=s/(569-1)
            cov[i][j]=s
    return cov

#Variable que guarda la matriz de datos estandarizada, es decir, con la resta del promedio y dividida en la desviacion estandar.
datosEstandarizados = estandariza(datamatrix)

matrizCov = cov_matrix(datosEstandarizados)




