"""
Laboratorio de Programación Básica en Python para Manejo de Datos
-----------------------------------------------------------------------------------------

Este archivo contiene las preguntas que se van a realizar en el laboratorio.

No puede utilizar pandas, numpy o scipy. Se debe utilizar solo las funciones de python
básicas.

Utilice el archivo `data.csv` para resolver las preguntas.


"""
import csv

def pregunta_01():
    """
    Retorne la suma de la segunda columna.

    Rta/
    214

    """
    sum = 0

    with open('data.csv', 'r') as file:
        csv_reader = csv.reader(file, delimiter = '\t')
        for row in csv_reader:
            sum += int(row[1])

    return sum


def pregunta_02():
    """
    Retorne la cantidad de registros por cada letra de la primera columna como la lista
    de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [
        ("A", 8),
        ("B", 7),
        ("C", 5),
        ("D", 6),
        ("E", 14),
    ]

    """
    letter_dict = {}
    letter_list = []

    with open('data.csv', 'r') as file:
        csv_reader = csv.reader(file, delimiter = '\t')
        for row in csv_reader:
            letter_dict[row[0]] = letter_dict.get(row[0], 0) + 1
    
    for key, value in letter_dict.items():
        letter_list.append((key, value))

    letter_list.sort()

    return letter_list


def pregunta_03():
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como una lista
    de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [
        ("A", 53),
        ("B", 36),
        ("C", 27),
        ("D", 31),
        ("E", 67),
    ]

    """
    letter_dict = {}
    letter_list = []

    with open('data.csv', 'r') as file:
        csv_reader = csv.reader(file, delimiter = '\t')
        for row in csv_reader:
            letter_dict[row[0]] = letter_dict.get(row[0], 0) + int(row[1])
    
    for key, value in letter_dict.items():
        letter_list.append((key, value))

    letter_list.sort()

    return letter_list


def pregunta_04():
    """
    La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la cantidad de
    registros por cada mes, tal como se muestra a continuación.

    Rta/
    [
        ("01", 3),
        ("02", 4),
        ("03", 2),
        ("04", 4),
        ("05", 3),
        ("06", 3),
        ("07", 5),
        ("08", 6),
        ("09", 3),
        ("10", 2),
        ("11", 2),
        ("12", 3),
    ]

    """
    month_dict = {}
    month_list = []

    with open('data.csv', 'r') as file:
        csv_reader = csv.reader(file, delimiter = '\t')
        for row in csv_reader:
            month = row[2][5:7]
            month_dict[month] = month_dict.get(month, 0) + 1
    
    for key, value in month_dict.items():
        month_list.append((key, value))

    month_list.sort()

    return month_list


def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2 por cada
    letra de la columa 1.

    Rta/
    [
        ("A", 9, 2),
        ("B", 9, 1),
        ("C", 9, 0),
        ("D", 8, 3),
        ("E", 9, 1),
    ]

    """
    letter_dict = {}
    letter_list = []

    with open('data.csv', 'r') as file:
        csv_reader = csv.reader(file, delimiter = '\t')
        for row in csv_reader:
            new_value = (row[1], row[1])
            letter_dict[row[0]] = (max(letter_dict.get(row[0], new_value)[0], new_value[0]), min(letter_dict.get(row[0], new_value)[1], new_value[1]))
    
    for key, value in letter_dict.items():
        letter_list.append(tuple(key) + value)

    letter_list.sort()

    return letter_list

def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras corresponde a
    una clave y el valor despues del caracter `:` corresponde al valor asociado a la
    clave. Por cada clave, obtenga el valor asociado mas pequeño y el valor asociado mas
    grande computados sobre todo el archivo.

    Rta/
    [
        ("aaa", 1, 9),
        ("bbb", 1, 9),
        ("ccc", 1, 10),
        ("ddd", 0, 9),
        ("eee", 1, 7),
        ("fff", 0, 9),
        ("ggg", 3, 10),
        ("hhh", 0, 9),
        ("iii", 0, 9),
        ("jjj", 5, 17),
    ]

    """
    strings = []
    char_dict = {}
    char_list = []

    with open('data.csv', 'r') as file:
        csv_reader = csv.reader(file, delimiter = '\t')
        for row in csv_reader:
            strings.append(row[4])

    for string in strings:
        str_splt = string.split(',')
        for element in str_splt:
            key = element.split(':')[0]
            values = (int(element.split(':')[1]), int(element.split(':')[1]))
            char_dict[key] = (min(char_dict.get(key, values)[0], values[0]), max(char_dict.get(key, values)[1], values[1]))

    for key, value in char_dict.items():
        char_list.append((key,) + value)

    char_list.sort()

    return char_list


def pregunta_07():
    """
    Retorne una lista de tuplas que asocien las columnas 0 y 1. Cada tupla contiene un
    valor posible de la columna 2 y una lista con todas las letras asociadas (columna 1)
    a dicho valor de la columna 2.

    Rta/
    [
        (0, ["C"]),
        (1, ["E", "B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E", "E", "D"]),
        (4, ["E", "B"]),
        (5, ["B", "C", "D", "D", "E", "E", "E"]),
        (6, ["C", "E", "A", "B"]),
        (7, ["A", "C", "E", "D"]),
        (8, ["E", "D", "E", "A", "B"]),
        (9, ["A", "B", "E", "A", "A", "C"]),
    ]

    """
    num_dict = {}
    num_list = []

    with open('data.csv', 'r') as file:
        csv_reader = csv.reader(file, delimiter = '\t')
        for row in csv_reader:
            number = int(row[1])
            num_dict[number] = num_dict.get(number, []) + list(row[0])

    for key, value in num_dict.items():
        num_list.append((key, value))

    num_list.sort()

    return num_list


def pregunta_08():
    """
    Genere una lista de tuplas, donde el primer elemento de cada tupla contiene  el valor
    de la segunda columna; la segunda parte de la tupla es una lista con las letras
    (ordenadas y sin repetir letra) de la primera  columna que aparecen asociadas a dicho
    valor de la segunda columna.

    Rta/
    [
        (0, ["C"]),
        (1, ["B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E"]),
        (4, ["B", "E"]),
        (5, ["B", "C", "D", "E"]),
        (6, ["A", "B", "C", "E"]),
        (7, ["A", "C", "D", "E"]),
        (8, ["A", "B", "D", "E"]),
        (9, ["A", "B", "C", "E"]),
    ]

    """
    num_dict = {}
    num_list = []

    with open('data.csv', 'r') as file:
        csv_reader = csv.reader(file, delimiter = '\t')
        for row in csv_reader:
            number = int(row[1])
            num_dict[number] = num_dict.get(number, []) + list(row[0])

    for key, value in num_dict.items():
        value = list(dict.fromkeys(value))
        value.sort()
        num_list.append((key, value))

    num_list.sort()

    return num_list


def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que aparece cada
    clave de la columna 5.

    Rta/
    {
        "aaa": 13,
        "bbb": 16,
        "ccc": 23,
        "ddd": 23,
        "eee": 15,
        "fff": 20,
        "ggg": 13,
        "hhh": 16,
        "iii": 18,
        "jjj": 18,
    }

    """
    strings = []
    char_dict = {}
    sorted_char_dict ={}

    with open('data.csv', 'r') as file:
        csv_reader = csv.reader(file, delimiter = '\t')
        for row in csv_reader:
            strings.append(row[4])

    for string in strings:
        str_splt = string.split(',')
        for element in str_splt:
            key = element.split(':')[0]
            char_dict[key] = char_dict.get(key, 0) + 1

    for k in sorted(char_dict):
        sorted_char_dict[k] = char_dict[k]

    return sorted_char_dict


def pregunta_10():
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la columna 1 y la
    cantidad de elementos de las columnas 4 y 5.

    Rta/
    [
        ("E", 3, 5),
        ("A", 3, 4),
        ("B", 4, 4),
        ...
        ("C", 4, 3),
        ("E", 2, 3),
        ("E", 3, 3),
    ]


    """
    elements_list = []

    with open('data.csv', 'r') as file:
        csv_reader = csv.reader(file, delimiter = '\t')
        for row in csv_reader:
            letter = row[0]
            fourth_row = len(row[3].split(','))
            fifth_row = len(row[4].split(','))
            elements_list.append((letter, fourth_row, fifth_row))
    
    return elements_list


def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada letra de la
    columna 4, ordenadas alfabeticamente.

    Rta/
    {
        "a": 122,
        "b": 49,
        "c": 91,
        "d": 73,
        "e": 86,
        "f": 134,
        "g": 35,
    }


    """
    letter_dict = {}
    sorted_letter_dict = {}

    with open('data.csv', 'r') as file:
        csv_reader = csv.reader(file, delimiter = '\t')
        for row in csv_reader:
            # string_list.append((int(row[1]), row[3]))
            number = int(row[1])
            letters = row[3].split(',')
            for letter in letters:
                letter_dict[letter] = letter_dict.get(letter, 0) + number

    for k in sorted(letter_dict):
        sorted_letter_dict[k] = letter_dict[k]

    return sorted_letter_dict


def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor la suma de
    los valores de la columna 5 sobre todo el archivo.

    Rta/
    {
        'A': 177,
        'B': 187,
        'C': 114,
        'D': 136,
        'E': 324
    }

    """
    char_dict = {}
    sorted_char_dict = {}

    with open('data.csv', 'r') as file:
        csv_reader = csv.reader(file, delimiter = '\t')
        for row in csv_reader:
            char = row[0]
            numbers = [int(x.split(':')[1]) for x in row[4].split(',')]
            char_dict[char] = char_dict.get(char, 0) + sum(numbers)

    for k in sorted(char_dict):
        sorted_char_dict[k] = char_dict[k]

    return sorted_char_dict