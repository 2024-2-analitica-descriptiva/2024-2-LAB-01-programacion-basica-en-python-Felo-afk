"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""

import csv


def pregunta_01():
    """
    Retorne la suma de la segunda columna.
    Rta/
    214
    """
    with open("files/input/data.csv", mode="r", encoding="utf-8") as arc:
        lector = csv.reader(arc, delimiter="\t")
        data = [fila for fila in lector]

    suma = sum(int(fila[1]) for fila in data)
    return suma


print(pregunta_01())
