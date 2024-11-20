"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""

import csv


def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada
    letra de la columna 4, ordenadas alfabeticamente.

    Rta/
    {'a': 122, 'b': 49, 'c': 91, 'd': 73, 'e': 86, 'f': 134, 'g': 35}


    """
    with open("files/input/data.csv", mode="r", encoding="utf-8") as arc:
        lector = csv.reader(arc, delimiter="\t")
        data = [fila for fila in lector]
    diccionario = {}

    for fila in data:
        letras = fila[3].split(",")
        valor = int(fila[1])

        for letra in letras:
            if letra in diccionario:
                diccionario[letra] += valor
            else:
                diccionario[letra] = valor
    return dict(sorted(diccionario.items()))


print(pregunta_11())
