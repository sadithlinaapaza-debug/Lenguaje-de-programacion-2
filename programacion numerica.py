import re

def analizar_expresion(expresion):
    variables = re.findall(r'[a-zA-Z_]\w*', expresion)

    operaciones = []
    if "+" in expresion:
        operaciones.append("suma (+)")
    if "-" in expresion:
        operaciones.append("resta (-)")
    if "*" in expresion:
        operaciones.append("multiplicación (*)")
    if "/" in expresion:
        operaciones.append("división (/)")
    if "" in expresion:
        operaciones.append("potencia ()")

    return set(variables), operaciones


# Entrada del usuario
expresion = input("Escribe una función o expresión matemática: ")

variables, operaciones = analizar_expresion(expresion)

print("\n--- RESULTADO ---")
print("Expresión ingresada:", expresion)
print("Variables encontradas:", variables if variables else "Ninguna")
print("Operaciones encontradas:", operaciones if operaciones else "Ninguna")
