import random


# Definir los datos de los Pokémon
pokemones = {
    "pikachu": {
        "vida_inicial": 90,
        "bola_voltio": 9,
        "onda_trueno": 11
    },
    "mew": {
        "vida_inicial": 75,
        "megapuno": 12,
        "coletazo": 9
    },
    "chatot": {
        "vida_inicial": 85,
        "ataque_furia": 11,
        "picotazon": 8
    }
}

# Seleccionar un Pokémon al azar
pokemon_seleccionado = random.choice(list(pokemones.keys()))

# Acceder a los datos del Pokémon seleccionado
datos_pokemon = pokemones[pokemon_seleccionado]

# Crear una lista con las habilidades del Pokémon, excluyendo "vida_inicial"
habilidades = [habilidad for habilidad in datos_pokemon.keys() if habilidad != "vida_inicial"]

# Seleccionar una habilidad al azar
habilidad_seleccionada = random.choice(habilidades)

print(f"El Pokémon seleccionado es: {pokemon_seleccionado}")
print(f"La habilidad seleccionada es: {habilidad_seleccionada}")
print(f"El valor de la habilidad seleccionada es: {datos_pokemon[habilidad_seleccionada]}")
print(f"El Pokémon seleccionado es: {pokemon_seleccionado}", datos_pokemon["vida_inicial"])
print(f"La habilidad seleccionada es: {habilidad_seleccionada}")
print(f"ataque es: {habilidad_seleccionada}")
print(f"El valor de la habilidad seleccionada es: {datos_pokemon[habilidad_seleccionada]}")
