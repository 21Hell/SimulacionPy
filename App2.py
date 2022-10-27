from tkinter import font
from turtle import update
import PySimpleGUI as sg
from Leer import leerNum
import generadorNumeros as gn
import Dados as d
import numpy as np
import generadores as gnd
import matplotlib as plt
import matplotlib.pyplot as plot

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

_VARS = {'window': False}

def draw_figure(canvas, figure):
    figure_canvas_agg = FigureCanvasTkAgg(figure, canvas)
    figure_canvas_agg.draw()
    figure_canvas_agg.get_tk_widget().pack(side='top', fill='both', expand=1)
    return figure_canvas_agg




AppFont = 'Any 16'
sg.theme('LightGrey')




#code to generate 3 tabs with 3 different layouts
layoutGenerados = []
layoutPruebas = []
layoutDados = []
layoutGeneradores = []

#code to create the window

window = sg.Window('Window Title', layoutGenerados, default_element_size=(40, 1), grab_anywhere=False)

#code to create the tabs
tab1 = sg.Tab('Tab 1', layoutGenerados, key='tab1')
tab2 = sg.Tab('Tab 2', layoutPruebas, key='tab2')
tab3 = sg.Tab('Tab 3', layoutDados, key='tab3')
tab4 = sg.Tab('Tab 4', layoutGeneradores, key='tab4')

layout = [[sg.TabGroup([[tab1, tab2, tab3, tab4]])]]

layoutGenerados = [[sg.Text('Generar numeros aleatorios')], [sg.Text('X0'), sg.InputText()], [sg.Text('K'), sg.InputText()], [sg.Text('G'), sg.InputText()], [sg.Button('Generar')]]
layoutPruebas = [[sg.Text('Pruebas de numeros aleatorios')], [sg.Button('Pruebas')]]
layoutDados = [[sg.Text('Dados')], [sg.Button('Dados')]]
layoutGeneradores = [[sg.Text('Generadores')], [sg.Button('Normal')], [sg.Button('Poisson')], [sg.Canvas(key='figCanvas')]]

window = sg.Window('Window Title', layout, default_element_size=(40, 1), grab_anywhere=False)

tab1.Layout(layoutGenerados)
tab2.Layout(layoutPruebas)
tab3.Layout(layoutDados)
tab4.Layout(layoutGeneradores)



#code to create the event loop












while True:
    event, values = window.read()
    valores = window.ReturnValuesList
    if event in (None, 'Exit'):
        break
    if event == 'tab1':
        window['-OUTPUT-'].update('Tab 1 was clicked')
    elif event == 'tab2':
        window['-OUTPUT-'].update('Tab 2 was clicked')
    elif event == 'tab3':
        window['-OUTPUT-'].update('Tab 3 was clicked')
    elif event == 'tab4':
        window['-OUTPUT-'].update('Tab 4 was clicked')
    
    if event == 'Generar':
        #fetch the values from the input fields

        x0 = int(valores[0])
        k = int(valores[1])
        g = int(valores[2])

        #convert the values to integers
        x0 = int(x0)
        k = int(k)
        g = int(g)


        #call the function to generate the random numbers
        s = gn.generar(x0, k, g)
        print(s)

    if event == 'Pruebas':
        #leer los numeros generados y hacer las pruebas
        ri = leerNum("numeros_aleatorios.csv")
        s = gn.pruebas()
        #mostrar s en un text box
        sg.popup(s)
    ri = leerNum("numeros_aleatorios.csv")
    if event == 'Dados':
        ri = leerNum("numeros_aleatorios.csv")
        d.simular_tiradas_dados(ri)
        dados = d.simular_tiradas_dados(ri)
        #mostrar en una grafica los resultados
        #popup que diga que se generaron las tiradas de dados
        sg.popup('Se generaron las tiradas de dados')
        #mostrar los resultados en una tabla
        sg.popup(dados)
        #indicar en un popup el intervalo de confianza con un titulo
        Intervalo = d.generar_intervalo_confianza_tiradas(d.obtener_medias_tiradas(dados))

        sg.popup('Intervalo de confianza', Intervalo)
        
    if event == 'Normal':
        ri = leerNum("numeros_aleatorios.csv")
        #generar numeros aleatorios con distribucion normal
        Norm = gnd.generadorNormal(6.5,40)
        #imprimir imagen de la distribucion normal
        plot.plot(Norm)
        plot.show()

    if event == 'Poisson':
        ri = leerNum("numeros_aleatorios.csv")
        #generar numeros aleatorios con distribucion poisson
        Poi = gnd.generadorPoisson(6.5)
        #imprimir imagen de la distribucion poisson
        plot.plot(Poi)
        plot.show()