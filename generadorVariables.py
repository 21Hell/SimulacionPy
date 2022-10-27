#Agregar librerias
from re import L
from turtle import goto
import numpy as np
import matplotlib.pyplot as plt
from Leer import leerNum
import math

    
l = leerNum("numeros_aleatorios.csv")
numeros = list(leerNum("numeros_aleatorios.csv"))
numerosPoiss = list(leerNum("numeros_aleatorios.csv"))
n = len(l)
i = 0
T = 1
#Funcion recursiva para generar distribucion normal apartir de valores ri
def generadorNormal(sd,mu):
    global numeros
    # numpy to list
    numeros = list(numeros)
    X = 0.0
    for i in range(12):
        X += numeros.pop(0)
    X -= 6
    X = sd*X + mu
    if X < 0:
        return generadorNormal(sd,mu)
    return X


def gPoisson(lam, N: int = 0, T: float = 1):
    Tp = T * l.pop(0)
    if Tp >= math.exp(-lam):
        N += 1
        T = Tp
        return gPoisson(lam, N, T)
    else:
        return N
        


def generadorExponencial(lamda):
    numeros = l
    ni = np.array([])
    i = 0
    for i in range(0,n-6,6):
        suma = numeros[i] + numeros[i+1] + numeros[i+2] + numeros[i+3] + numeros[i+4] + numeros[i+5]
        ni = np.append(ni, -np.log(1-suma)/lamda)
    return ni