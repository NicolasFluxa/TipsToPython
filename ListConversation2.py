

lista = [1,2,3, "a", 4,5]
# list convergetion con una funcion de python la cual devuevle un True o False
# en este caso ve si el valor que tiene "i" es "int" de ser Devuelve un True
# Por lo tanto agrega ese valor a la lista creada

print([i for i in lista if isinstance(i, int)])