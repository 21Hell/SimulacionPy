#Generar una funcion para leer los datos del documento csv

import numpy as np

def leerNum(file):
    out = []
    with open(file, 'r') as f:
        for linea in f:
            out.append(float(linea))
    return out

def leerString(file):
    out = []
    with open(file, 'r') as f:
        for linea in f:
            out.append(linea)
    return out