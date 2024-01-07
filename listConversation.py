primera_lista = []

segunda_lista = []
for a in primera_lista:
    segunda_lista.append(a.lower())

# Resume lo anterior a solo una linea
[a.lower() for a in primera_lista]
