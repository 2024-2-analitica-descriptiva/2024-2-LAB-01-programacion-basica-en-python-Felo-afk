"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""

import csv


def pregunta_03():
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como
    una lista de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [('A', 53), ('B', 36), ('C', 27), ('D', 31), ('E', 67)]

    """
    with open("files/input/data.csv", mode="r", encoding="utf-8") as arc:
        lector = csv.reader(arc, delimiter="\t")
        data = [fila for fila in lector]
    col1 = [(x[0], int(x[1])) for x in data]
    shuffle = sorted(col1, key=lambda x: x[0])
    diccionario = {}
    for key, value in shuffle:
        if key in diccionario:
            diccionario[key] += value
        else:
            diccionario[key] = value

    return list(diccionario.items())
