#Agregar librerias
from re import L
import numpy as np
import matplotlib.pyplot as plt
from Leer import leerNum


l = leerNum("numeros_aleatorios.csv")
n = len(l)

#Funcion recursiva para generar distribucion normal apartir de valores ri
def generadorNormal(sd,mu):
    numeros = l
    ni = np.array([])
    i = 0
    for i in range(0,n-6,6):
        suma = numeros[i] + numeros[i+1] + numeros[i+2] + numeros[i+3] + numeros[i+4] + numeros[i+5]
        print(suma)
        ni = np.append(ni, sd*suma+mu)
    return ni


#Funcion para imprimir histograma en consola
def imprimirHistograma(ni):
    plt.hist(ni, bins=20)
    plt.show()

#Funcion para imprimir histograma en archivo
def imprimirHistogramaArchivo(ni):
    plt.hist(ni, bins=20)
    plt.savefig("histogramaNormal.png")



def generadorPoisson(lamda):
    numeros = l
    ni = np.array([])
    T = 1
    N = 0
    i = 0
    #euler number
    e = 2.718281828459045
    for i in range(0,n):
        Tprima = T*(numeros[i])
        print (Tprima)
        if Tprima > e**(-lamda):
            N = N + 1
            T = Tprima
        elif Tprima < e**(-lamda):
            ni = np.append(ni, N)
    return ni


def generadorExponencial(lamda):




    return ni