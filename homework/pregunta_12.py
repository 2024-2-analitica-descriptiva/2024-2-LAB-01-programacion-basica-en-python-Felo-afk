"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""

import csv


def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor
    la suma de los valores de la columna 5 sobre todo el archivo.

    Rta/
    {'A': 177, 'B': 187, 'C': 114, 'D': 136, 'E': 324}

    """

    with open("files/input/data.csv", mode="r", encoding="utf-8") as arc:
        lector = csv.reader(arc, delimiter="\t")
        data = [fila for fila in lector]
    diccionario = {}

    diccionario = {}

    for fila in data:
        clave = fila[0]
        valores = sum(int(par.split(":")[1]) for par in fila[4].split(","))

        if clave in diccionario:
            diccionario[clave] += valores
        else:
            diccionario[clave] = valores

    return dict(sorted(diccionario.items()))


print(pregunta_12())
