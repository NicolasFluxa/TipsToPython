import random as rd


lista = [rd.randint(1, 11) for i in list(range(1, 11))]
valorMenor = lista[0]
valorMayor = lista[0]

for num in lista:
    if num < valorMenor:
        valorMenor = num
    elif num > valorMayor:
        valorMayor = num

print(lista)
print(valorMenor)
print(valorMayor)
