# forma poco eficiente
archivo = "nombre"
listaSupermercado = []


a = open(archivo + ".txt", "w")
a.write("\n".join(listaSupermercado))
a.close()

# forma eficiente y breve
# lo abre le la los permisos y dice hasta donde
#
with open(archivo + ".txt", "w") as archivo:
    archivo.write("\n".join(listaSupermercado))
