"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""

import csv


def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras
    corresponde a una clave y el valor despues del caracter `:` corresponde al
    valor asociado a la clave. Por cada clave, obtenga el valor asociado mas
    pequeño y el valor asociado mas grande computados sobre todo el archivo.

    Rta/
    [('aaa', 1, 9),
     ('bbb', 1, 9),
     ('ccc', 1, 10),
     ('ddd', 0, 9),
     ('eee', 1, 7),
     ('fff', 0, 9),
     ('ggg', 3, 10),
     ('hhh', 0, 9),
     ('iii', 0, 9),
     ('jjj', 5, 17)]

    """
    with open("files/input/data.csv", mode="r", encoding="utf-8") as arc:
        lector = csv.reader(arc, delimiter="\t")
        data = [fila for fila in lector]
    diccionario = []
    [diccionario.extend(x[4].split(",")) for x in data]

    diccionario = [tuple(x.split(":")) for x in diccionario]
    elementos = set(fila[0] for fila in diccionario)
    res = [
        (
            elemento,
            min(int(fila[1]) for fila in diccionario if fila[0] == elemento),
            max(int(fila[1]) for fila in diccionario if fila[0] == elemento),
        )
        for elemento in elementos
    ]
    return sorted(res, key=lambda x: x[0])


print(pregunta_06())
