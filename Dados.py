#importar librerias
import numpy as np
from scipy import stats
import collections

from Leer import leerNum

l = leerNum("numeros_aleatorios.csv")

def simular_tiradas_dados(numeros):
    numeros_aleatorios = numeros
    #dividir numeros aleatorios en 50 grupos
    grupos = []
    for i in range(0, len(numeros_aleatorios), 50):
        grupos.append(numeros_aleatorios[i:i + 50])

    #para cada grupo, simular 50 tiradas de dados
    tiradas = []
    for grupo in grupos:
        tirada = []
        for numero in grupo:
            if numero < 1 / 6:
                tirada.append(1)
            elif numero < 2 / 6:
                tirada.append(2)
            elif numero < 3 / 6:
                tirada.append(3)
            elif numero < 4 / 6:
                tirada.append(4)
            elif numero < 5 / 6:
                tirada.append(5)
            else:
                tirada.append(6)
        tiradas.append(tirada)
    return tiradas

tiradas = simular_tiradas_dados(leerNum("numeros_aleatorios.csv"))

def obtener_medias_tiradas(tiradas):
    medias = []
    for tirada in tiradas:
        medias.append(np.mean(tirada))
    return medias

def obtener_varianzas_tiradas(tiradas):
    varianzas = []
    for tirada in tiradas:
        varianzas.append(np.var(tirada))
    return varianzas

def obtener_frecuencias_tiradas(tiradas):
    frecuencias = []
    for tirada in tiradas:
        frecuencias.append(collections.Counter(tirada))
    return frecuencias

def obtener_modas_tiradas(tiradas):
    modas = []
    for tirada in tiradas:
        modas.append(stats.mode(tirada))
    return modas


def mostrar_distribucion_tiradas(tiradas):
    medias = obtener_medias_tiradas(tiradas)
    varianzas = obtener_varianzas_tiradas(tiradas)
    modas = obtener_modas_tiradas(tiradas)
    mediaDeMedias = np.mean(medias)
    varianzaDeMedias = np.var(medias)
    print("Media de las medias: ", np.mean(medias))
    print("Varianza de las medias: ", np.var(medias))
    print("Media de las varianzas: ", np.mean(varianzas))
    print("Varianza de las varianzas: ", np.var(varianzas))
    print("Media de las modas: ", np.mean(modas))
    print("Varianza de las modas: ", np.var(modas))



def generar_intervalo_confianza_tiradas(tiradas):
    intervalos = []
    intervalos.append(stats.t.interval(0.95, len(tiradas) - 1, loc = np.mean(tiradas), scale = stats.sem(tiradas)))
    return intervalos

print("Intervalo de confianza para las medias: ", generar_intervalo_confianza_tiradas(obtener_medias_tiradas(tiradas)))