"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""

import csv


def pregunta_04():
    """
    La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la
    cantidad de registros por cada mes, tal como se muestra a continuación.

    Rta/
    [('01', 3),
     ('02', 4),
     ('03', 2),
     ('04', 4),
     ('05', 3),
     ('06', 3),
     ('07', 5),
     ('08', 6),
     ('09', 3),
     ('10', 2),
     ('11', 2),
     ('12', 3)]

    """
    with open("files/input/data.csv", mode="r", encoding="utf-8") as arc:
        lector = csv.reader(arc, delimiter="\t")
        data = [fila for fila in lector]
    col1 = [x[2].split("-") for x in data]
    col1 = [x[1] for x in col1]
    mapper = [(word, 1) for word in col1]
    shuffle = sorted(mapper, key=lambda x: x[0])
    diccionario = {}
    for key, value in shuffle:
        if key in diccionario:
            diccionario[key] += value
        else:
            diccionario[key] = value

    return list(diccionario.items())


print(pregunta_04())
