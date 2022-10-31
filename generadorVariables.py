#Agregar librerias
from re import L
from turtle import goto
import numpy as np
import matplotlib.pyplot as plt
from Leer import leerNum
import math
from scipy import stats as st
from cmath import sqrt

    
l = leerNum("numeros_aleatorios.csv")
numeros = list(leerNum("numeros_aleatorios.csv"))
numerosPoiss = list(leerNum("numeros_aleatorios.csv"))
n = len(l)
i = 0
T = 1
#Funcion recursiva para generar distribucion normal apartir de valores ri
def gNormal(sd,mu):
    global numeros
    # numpy to list
    numeros = list(numeros)
    X = 0.0
    for i in range(12):
        X += numeros.pop(0)
    X -= 6
    X = sd*X + mu
    if X < 0:
        return gNormal(sd,mu)
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



n = [gNormal(6.5,10) for i in range(100)]
inc = (abs(min(n)) + max(n)) / sqrt(len(n)).real
p = min(n)
intervalos = []
for i in range(10):
    intervalos.append([p, p + inc])
    p += inc

#Calculo Oi
Oi = np.zeros(int(sqrt(len(n)).real))
for j in range(len(intervalos)):
    for i in range(len(n)):
        if n[i] <= intervalos[j][1] and n[i] >= intervalos[j][0]:
            Oi[j] += 1

#Calculo de P(x)
Px = np.zeros(int(sqrt(len(n)).real))
for i in range(len(Px)):
    if i != len(Px) - 1:
        Px[i] = st.norm.cdf(intervalos[i][1], 10, 6.5) - st.norm.cdf(intervalos[i][0], 10, 6.5)
Px[len(Px) - 1] = 1 - sum(Px)

#Calculo de Ei
Ei = np.zeros(int(sqrt(len(n)).real))
for i in range(len(Ei)):
    Ei[i] = len(n) * Px[i]

#Calculo de Chi
print(st.chi2.isf(0.05, 100))

#Imprimir en csv
with open('Chi.csv', 'w') as c:
    c.write('Intervalo, P(x), Oi, Ei, Error\n')
    for i in range(len(intervalos)):
        c.write(f'{intervalos[i][0]} - {intervalos[i][1]}, {Px[i]}, {Oi[i]}, {Ei[i]}, {((Oi[i] - Ei[i])**2)/Ei[i]}\n')