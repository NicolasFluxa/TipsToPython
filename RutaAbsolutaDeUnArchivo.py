import glob
import os
from TipsToPython import EncuentraRutas


def rutas_funciones():
    # con esto encuentro el nombre del usuario
    listaCarpetas = glob.glob(EncuentraRutas.obten_Ruta_absoluta_Total())
    print(listaCarpetas)
    # Lo que hace esto es poner la lista "listacarpetas" en al reves
    # Pero tambien podemos agregar otras funciones o otras formas de ordenar las cosa
    listaCarpetas.sort(reverse=True)
    print(listaCarpetas)
    # Con el len lo ordenara por tamaño cada item de la carpeta
    listaCarpetas.sort(key=len, reverse=True)
    print(listaCarpetas)
    # Lo que hace esto es ordenar por la fecha de modificacion de cada uno de las carpetas
    listaCarpetas.sort(key=os.path.getmtime)
    print(listaCarpetas)


def main():
    rutas_funciones()


if __name__ == "__main__":
    main()
