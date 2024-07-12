primera_lista = [1,2,3,4,5,6,7]

segunda_lista = []
for a in primera_lista:
    segunda_lista.append(str(a))

# Resume lo anterior a solo una linea
[str(a) for a in primera_lista]

print(primera_lista)
print(segunda_lista)
print([str(a) for a in primera_lista])
print(primera_lista)