# Crea un codigo que verifique si el numero o palabra es un
# Palindromo
# Ejemplo: input: reconocer ; output: True, input 121 : output: True


valor = input("Ingrese el valor")
print(valor == valor[::-1])