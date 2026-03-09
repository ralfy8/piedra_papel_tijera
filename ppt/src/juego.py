import random

def mostrar_opciones():
    print("Elige una opción:")
    print("1 - Piedra")
    print("2 - Papel")
    print("3 - Tijera")

def mostrar_opciones():
    print("Elige una opción:")
    print("1 - Piedra")
    print("2 - Papel")
    print("3 - Tijera")

def convertir_numero_a_eleccion(numero):
    if numero == "1":
        return "Piedra"
    elif numero == "2":
        return "Papel"
    elif numero == "3":
        return "Tijera"
    else:
        return None

