import os


def obten_Ruta_absoluta_Total():

    nombre_usuario = os.path.expanduser("~*")

    return nombre_usuario


def obten_Nombre_usuario():
    nombre_usuario = os.path.expanduser("~")

    return nombre_usuario
