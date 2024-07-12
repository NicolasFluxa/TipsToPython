
"""
Escribir un programa que pregunte por consola por los productos
de una cesta de la compra, separados por comas, y muestre por
pantalla cada uno de los productos en una línea distinta.
"""

lista_compra = input("lista")
lista_compra = lista_compra.split(", ")
for i in lista_compra:
    print(i)
