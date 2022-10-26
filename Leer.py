#Generar una funcion para leer los datos del documento csv

import numpy as np

def leerNum(file):
    out = np.array([])
    with open(file, 'r') as f:
        for linea in f:
            out = np.append(out, float(linea))
    return out

def leerString(file):
    out = []
    with open(file, 'r') as f:
        for linea in f:
            out.append(linea)
    return out