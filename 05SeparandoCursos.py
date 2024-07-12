
"""
Los alumnos de un curso se han dividido en dos grupos A y B de acuerdo al sexo y el nombre.
El grupo A esta formado por las mujeres con un nombre anterior a la M y los hombres con un
nombre posterior a la N y el grupo B por el resto. Escribir un programa que pregunte al
usuario su nombre y sexo, y muestre por pantalla el grupo que le corresponde.

mujeres A-M Y hombres N-Z grupo A
mujeres N-Z Y hombres A-M Grupo B
"""
valor = input("apellido")
valor2 = input("sexo")
listaa = []
listab = []

if valor[0] < "m" and valor2 == "mujer" or valor[0] > "m" and valor2 == "hombre":
    listaa.append(valor)
    print(listaa, "A")
else:
    listab.append(valor)
    print(listab)