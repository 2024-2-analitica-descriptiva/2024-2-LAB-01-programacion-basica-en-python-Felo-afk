"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""

import csv


def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que
    aparece cada clave de la columna 5.

    Rta/
    {'aaa': 13,
     'bbb': 16,
     'ccc': 23,
     'ddd': 23,
     'eee': 15,
     'fff': 20,
     'ggg': 13,
     'hhh': 16,
     'iii': 18,
     'jjj': 18}

    """
    with open("files/input/data.csv", mode="r", encoding="utf-8") as arc:
        lector = csv.reader(arc, delimiter="\t")
        data = [fila for fila in lector]
    claves = []
    [claves.extend(x[4].split(",")) for x in data]

    claves = [tuple(x.split(":")) for x in claves]
    claves = [x[0] for x in claves]
    mapper = [(word, 1) for word in claves]
    shuffle = sorted(mapper, key=lambda x: x[0])
    diccionario = {}
    for key, value in shuffle:
        if key in diccionario:
            diccionario[key] += value
        else:
            diccionario[key] = value

    return dict(diccionario.items())


print(pregunta_09())
