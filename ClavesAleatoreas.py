import random
import string

# Crea una cadena que contiene letras minúsculas, mayúsculas y signos de puntuación
# Selecciona 15 caracteres aleatorios de la cadena

caracteres = string.ascii_lowercase + string.ascii_uppercase + string.punctuation

"""Esto es la forma rapida de hacer lo de abajo"""
cadena_aleatoria = "".join(random.choice(caracteres) for letra in range(40))

"""Esta es la forma lenta de hacer lo de arriba"""
cadena_aleatoria2 = []
for item in range(40):
    cadena_aleatoria2.append(random.choice(caracteres))

print(cadena_aleatoria)
print("".join(cadena_aleatoria2))
