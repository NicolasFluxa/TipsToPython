import os

# si quiero listar todas las carpetas que están dentro de otra ocupas
# Esto nos da el usuario
direccion = os.path.expanduser("~")

# dentro de los paréntesis ponemos el path de la carpeta a revisar
lista_de_carpetas = os.listdir(direccion)

def muestra():
    for i in range(len(lista_de_carpetas)):
        print(lista_de_carpetas[i])


def main():
    muestra()


if __name__ == '__main__':
    main()
