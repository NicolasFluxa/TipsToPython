# Desarrolla una calculadora de numeros romanos,
# input: MDXI ; output: 1511

"""Tiene un error IV es 4 no 6"""

dicc = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

romano = input("Ingrese las letras\n").upper()
suma = 0

for i in range(0, len(romano)):
    suma += dicc[romano[i]]

print(suma)

