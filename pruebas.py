#importar librerias
import numpy as np

from Leer import leerNum
from scipy import stats

l = leerNum("numeros_aleatorios.csv")
n = len(l)

def prueba_arriba_abajo_media():
    numeros_aleatorios = l
    media = np.mean(numeros_aleatorios)
    arriba_media = 0
    abajo_media = 0
    for numero in numeros_aleatorios:
        if numero > media:
            arriba_media += 1
        else:
            abajo_media += 1
    print("Arriba de la media: ", arriba_media)
    print("Abajo de la media: ", abajo_media)
    print("Media: ", media)
    print("Diferencia: ", arriba_media - abajo_media)
    print("Diferencia porcentual: ", (arriba_media - abajo_media) / n * 100)
    print("Diferencia esperada: ", n / 2 * 0.01)
    print("Diferencia esperada porcentual: ", n / 2 * 0.01 / n * 100)
    #Imprimir si se acepta o no la hipotesis nula
    if (arriba_media - abajo_media) / n * 100 < n / 2 * 0.01 / n * 100:
        return "Prueba Arriba y Abajo de la Media (Independencia) Se acepta la hipotesis"
    else:
        return "Prueba Arriba y Abajo de la Media (Independencia) Se rechaza la hipotesis"
#Realizar prueba de varianza
def prueba_varianza():
    numeros_aleatorios = l
    #Obtener varianza
    varianza = np.var(numeros_aleatorios)
    #chi superior
    chi_superior = stats.chi2.ppf(q = 0.975, df = n - 1)
    #chi inferior
    chi_inferior = stats.chi2.ppf(q = 0.025, df = n - 1)
    #Obtener varianza esperada
    varianza_esperada = (chi_superior - chi_inferior) / 2
    if varianza < varianza_esperada:
        return "Varianza: Se acepta la hipotesis"
    else:
        return "Varianza: Se rechaza la hipotesis"

#pureba de Chi cuadrada
def prueba_chi_cuadrada():
    numeros_aleatorios = l
    #Obtener frecuencia de cada numero
    frecuencias = {}
    for numero in numeros_aleatorios:
        if numero in frecuencias:
            frecuencias[numero] += 1
        else:
            frecuencias[numero] = 1
    #Obtener frecuencia esperada
    frecuencia_esperada = n / len(frecuencias)
    #Obtener estadistico de prueba
    estadistico_prueba = 0
    for numero in frecuencias:
        estadistico_prueba += (frecuencias[numero] - frecuencia_esperada) ** 2 / frecuencia_esperada
    print("Estadistico de prueba: ", estadistico_prueba)
    #Obtener valor critico
    valor_critico = stats.chi2.ppf(q = 0.95, df = len(frecuencias) - 1)
    print("Valor critico: ", valor_critico)
    #Imprimir si se acepta o no la hipotesis nula
    if estadistico_prueba < valor_critico:
        return "Prueba Chi Cuadrada Se acepta la hipotesis"
    else:
        return "Prueba Chi Cuadrada Se rechaza la hipotesis"

#Prueba de medias
def prueba_medias():
    numeros_aleatorios = l
    #Obtener frecuencia de cada numero
    frecuencias = {}
    for numero in numeros_aleatorios:
        if numero in frecuencias:
            frecuencias[numero] += 1
        else:
            frecuencias[numero] = 1
    #Obtener frecuencia esperada
    frecuencia_esperada = n / len(frecuencias)
    #Obtener estadistico de prueba
    estadistico_prueba = 0
    for numero in frecuencias:
        estadistico_prueba += (frecuencias[numero] - frecuencia_esperada) ** 2 / frecuencia_esperada
    print("Estadistico de prueba: ", estadistico_prueba)
    #Obtener valor critico
    valor_critico = stats.chi2.ppf(q = 0.95, df = len(frecuencias) - 1)
    print("Valor critico: ", valor_critico)
    #Imprimir si se acepta o no la hipotesis nula
    if estadistico_prueba < valor_critico:
        return "Prueba Medias Se acepta la hipotesis"
    else:
        return "Prueba Medias Se rechaza la hipotesis"

