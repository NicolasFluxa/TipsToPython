
""""
Escribir un programa que pregunte el nombre del usuario en la consola
 y un número entero e imprima por pantalla en líneas distintas el nombre
 del usuario tantas veces como el número introducido.
"""
nombre = list(input("Ingrese su nombre seguido de un numero del 1 - 10"))
lista_numeros = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]

for item in nombre:
    if item in lista_numeros:
        valor = int(nombre[nombre.index(item)])
        nombre.pop(nombre.index(item))
        print(("".join(nombre) * valor))
