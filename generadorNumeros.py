import pruebas as pb



#importar librerias
import numpy as np

from Leer import leerNum
from scipy import stats


def obtener_c(m):
    c = m - 1
    while (m % c == 0):
        c -= 1
    return c
#Generar funcion de numeros aleatorios
def generar_numeros_aleatorios(x0, c, g, m, n):
    numeros_aleatorios = []
    for i in range(n):
        x0 = (g * x0 + c) % m
        numeros_aleatorios.append(x0)
    return numeros_aleatorios

#con los numeros aleatorios guardarlos en un documento csv
def guardar_numeros_aleatorios(numeros_aleatorios):
    with open('numeros_aleatorios.csv', 'w') as f:
        for numero in numeros_aleatorios:
            f.write(str(numero) + '\n')

def obtener_numeros_aleatorios(x0, c, g, m, n):
    numeros_aleatorios = generar_numeros_aleatorios(x0, c, g, m, n)
    numeros_aleatorios = [numero / m for numero in numeros_aleatorios]
    return numeros_aleatorios

#Generar los numeros aleatorios
def generar(X0, g, k):
    x0 = X0
    k = k
    g = g
    m = 2**k
    n = m
    c = obtener_c(int(m))
    numeros_aleatorios = obtener_numeros_aleatorios(x0, c, g, m, n)
    guardar_numeros_aleatorios(numeros_aleatorios)
    #en el messagebox mostrar los datos de la simulacion X0, g, k, m, c, n
    return ("Simulacion", "X0: " + str(x0) + "\n" + "g: " + str(g) + "\n" + "k: " + str(k) + "\n" + "m: " + str(m) + "\n" + "c: " + str(c) + "\n" + "n: " + str(n))
    #Bloquear los datos de entrada
    
def pruebas():
    s = pb.prueba_medias()
    s += "\n" + pb.prueba_varianza()
    s += "\n" + pb.prueba_chi_cuadrada()
    s += "\n" + pb.prueba_arriba_abajo_media()
    return "Resultados: " + s
