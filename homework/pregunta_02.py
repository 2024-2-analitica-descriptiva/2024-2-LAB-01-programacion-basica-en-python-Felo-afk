"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""

import csv


def pregunta_02():
    """
    Retorne la cantidad de registros por cada letra de la primera columna como
    la lista de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [('A', 8), ('B', 7), ('C', 5), ('D', 6), ('E', 14)]

    """
    with open("files/input/data.csv", mode="r", encoding="utf-8") as arc:
        lector = csv.reader(arc, delimiter="\t")
        data = [fila for fila in lector]
    col1 = [x[0] for x in data]
    mapper = [(word, 1) for word in col1]
    shuffle = sorted(mapper, key=lambda x: x[0])
    diccionario = {}
    for key, value in shuffle:
        if key in diccionario:
            diccionario[key] += value
        else:
            diccionario[key] = value

    return list(diccionario.items())


print(pregunta_02())
