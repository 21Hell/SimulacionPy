#Crear una app visual usando Custom Tkinter 
#Importar librerias
from cgitb import text
from socket import CAN_BCM_RX_TIMEOUT
from tkinter import *
from tkinter import Frame, Label, Entry, Button, messagebox, ttk
from unicodedata import numeric
import pruebas as pb
import Dados as d
from Leer import leerNum
import numpy as np
import matplotlib

import PIL
from PIL import TkImage
from PIL import Image



#Crear tabs
root = Tk()
root.title("Simulacion de numeros aleatorios")
root.geometry("500x500")
root.resizable(0, 0)
#Crear tabs
tab_control = ttk.Notebook(root)


tab1 = ttk.Frame(tab_control)
tab_control.add(tab1, text="Generar numeros aleatorios")
tab_control.pack(expand=1, fill="both")

#Crear tab de Dados
tab2 = ttk.Frame(tab_control)
tab_control.add(tab2, text="Simular tiradas de dados")
tab_control.pack(expand=1, fill="both")



    
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
def generar():
    x0 = int(entry_x0.get())
    k = int(entry_k.get())
    g = int(entry_g.get())
    m = 2**k
    n = m
    c = obtener_c(int(m))
    numeros_aleatorios = obtener_numeros_aleatorios(x0, c, g, m, n)
    guardar_numeros_aleatorios(numeros_aleatorios)
    #en el messagebox mostrar los datos de la simulacion X0, g, k, m, c, n
    messagebox.showinfo("Simulacion", "X0: " + str(x0) + "\n" + "g: " + str(g) + "\n" + "k: " + str(k) + "\n" + "m: " + str(m) + "\n" + "c: " + str(c) + "\n" + "n: " + str(n))
    #Bloquear los datos de entrada
    
def pruebas():
    s = pb.prueba_medias()
    s += "\n" + pb.prueba_varianza()
    s += "\n" + pb.prueba_chi_cuadrada()
    s += "\n" + pb.prueba_arriba_abajo_media()
    messagebox.showinfo("Resultados", s)


numeros = leerNum("numeros_aleatorios.csv")

def leerDatos():
    global numeros
    numeros = leerNum("numeros_aleatorios.csv")


def tirarDados():
    global numeros
    dados = d.simular_tiradas_dados(numeros)
    #mostrar en una grafica los resultados
    fig = Figure(figsize=(5, 5), dpi=100)
    a = fig.add_subplot(111)
    a.plot(dados)
    canvas = FigureCanvasTkAgg(fig, master=tab2)
    canvas.show()
    canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)
    toolbar = NavigationToolbar2TkAgg(canvas, tab2)
    toolbar.update()
    canvas._tkcanvas.pack(side=TOP, fill=BOTH, expand=1)












#en el tab1 crear los labels, entrys y botones
label_x0 = Label(tab1, text="X0")
label_x0.grid(row=0, column=0, padx=5, pady=5)
entry_x0 = Entry(tab1)
entry_x0.grid(row=0, column=1, padx=5, pady=5)
label_g = Label(tab1, text="g")
label_g.grid(row=1, column=0, padx=5, pady=5)
entry_g = Entry(tab1)
entry_g.grid(row=1, column=1, padx=5, pady=5)
label_k = Label(tab1, text="k")
label_k.grid(row=2, column=0, padx=5, pady=5)
entry_k = Entry(tab1)
entry_k.grid(row=2, column=1, padx=5, pady=5)
button_generar = Button(tab1, text="Generar", command=generar)
button_generar.grid(row=3, column=0, columnspan=2, padx=5, pady=5)
#boton pruebas
button_pruebas = Button(tab1, text="Pruebas", command=pruebas)
button_pruebas.grid(row=4, column=0, columnspan=2, padx=5, pady=5)







    
#en el tab2 crear los labels, entrys y botones
label_dados = Label(tab2, text="Simular tiradas de dados")
label_dados.grid(row=0, column=0, padx=5, pady=5)

#Crear un boton para leer los datos
button_leer = Button(tab2, text="Leer", command=leerDatos)
button_leer.grid(row=1, column=0, columnspan=2, padx=5, pady=5)

#Crear un boton para simular las tiradas de dados
button_tirar = Button(tab2, text="Tirar", command=tirarDados)
button_tirar.grid(row=2, column=0, columnspan=2, padx=5, pady=5)







root.mainloop()