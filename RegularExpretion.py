import re

# re.search busca el patron 'Hola' en la cadena ?Hola, Mundo'. Si el patron
# se encuentra en la cadena, Se imprime ,Se encontró el patrón.
# De lo contrario, se imprime 'No se encontró el patrón

cadena = 'Hola, mundo, hola'
patron = 'Hola'

resultado = re.search(patron, cadena)

if resultado:
    print('Se encontró el patrón.')
else:
    print('No se encontró el patrón.')
