# Definimos la función main que toma cuatro argumentos: x, y, z, n
def main(x, y, z, n):
    # Inicializamos una lista vacía llamada lista2
    lista2 = []
    # Iteramos sobre el rango de 0 a x (incluyendo x)
    for i in range(x+1):
        # Iteramos sobre el rango de 0 a y (incluyendo y)
        for j in range(y+1):
            # Iteramos sobre el rango de 0 a z (incluyendo z)
            for k in range(z+1):
                # Verificamos si la suma de i, j, k no es igual a n
                if (i + j + k) != n:
                    # Si la condición es verdadera, creamos una lista con i, j, k
                    lista = [i, j ,k]
                    # Agregamos la lista a lista2
                    lista2.append(lista)
    # Imprimimos lista2
    print(lista2)

# Verificamos si este archivo se está ejecutando como el archivo principal
if __name__ == '__main__':
    # Solicitamos al usuario que ingrese los valores de x, y, z, n
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    # Llamamos a la función main con los valores ingresados
    main(x, y, z, n)
