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

#esta variable guarda la matriz de covarianza, hecha con la implementacion propia.
matrizCov = cov_matrix(datosEstandarizados)



#Calcule los autovalores y autovectores de la matriz de covarianza y los imprima (para estopuede usar los paquetes de linalg de numpy). Su mensaje debe indicar explicitamente cual es cada autovector y su autovalor correspondiente.
eigvalues,eigvectors = np.linalg.eig(matrizCov)

print "Estos son los valores propios de la matriz de covarianza: "
print eigvalues
print "Estos son los vectores propios de la matriz de covarianza: "
print eigvectors

#Imprima un mensaje que diga cuales son los parametros mas importantes en base a las componentes de los autovectores.


print "Los parametros mas importantes son los dos primeros, dado que son los dos primeros autovalores los que tienen la magnitud mas grande, y eso nos dice que son los parametros que mas informacion contiene sobre el fenomeno que se esta estudiando."



#Haga una proyeccion de sus datos en el sistema de coordenadas PC1, PC2 y grafique estos datos. Use un color distinto para el diagnostico maligno y el benigno y la guarde dicha grafica sin mostrarla en ApellidoNombre_PCA.pdf.



# Hay una parte del codigo que tiene un error que no se como arreglar pero se que el codigo no esta del todo mal.
mal=[]
bien=[]
for i in range(len(vectorMoB)):
	if(vectorMoB[i]==1):
		mal.append(i)
	else:
		bien.append(i)


#malignos=[]
#benignos=[]
#for i in range(len(mal)):		
	#malignos.append(datosEstandarizados[mal[i]])	

#for i in range(len(bien)):
	#benignos.append(datosEstandarizados[bien[i]])

#cancerSi= np.matmul(malignos,eigvectors)
#cancerNo= np.matmul(benignos,eigvectors)
	
#plt.figure()
#plt.scatter(cancerSi[:,0],cancerSi[:,1],label="M")
#plt.scatter(cancerNo[:,0],cancerNo[:,1],color="red",label="B")
#plt.legend(loc='lower left')
#plt.xlabel("PC2")
#plt.ylabel("PC1")
#plt.savefig("LoaizaDaniel_PCA.pdf")



#Imprima un mensaje diciendo si el metodo de PCA es util para hacer esta clasificacion, sino sirve o si puede ayudar al diagnostico para ciertos pacientes, argumentando claramente su posicion.


print "Si es muy util porque PCA separa en dos grandes grupos los pacientes que tienen diagnostico maligno o benigno, ademas si conocemos cuales son los dos parametros que mayor poder de predidiccion tienen sobre el fenomeno en cuestion, PCA reduce la cantidad de informacion con la que se debe trabajar de manera optima"









