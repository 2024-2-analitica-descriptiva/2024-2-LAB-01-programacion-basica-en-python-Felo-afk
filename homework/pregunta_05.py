"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""

import csv


def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2
    por cada letra de la columa 1.

    Rta/
    [('A', 9, 2), ('B', 9, 1), ('C', 9, 0), ('D', 8, 3), ('E', 9, 1)]

    """
    with open("files/input/data.csv", mode="r", encoding="utf-8") as arc:
        lector = csv.reader(arc, delimiter="\t")
        data = [fila for fila in lector]
    letras = set(fila[0] for fila in data)
    resultado = [
        (
            letra,
            int(max(fila[1] for fila in data if fila[0] == letra)),
            int(min(fila[1] for fila in data if fila[0] == letra)),
        )
        for letra in letras
    ]
    return sorted(resultado, key=lambda x: x[0])


print(pregunta_05())
