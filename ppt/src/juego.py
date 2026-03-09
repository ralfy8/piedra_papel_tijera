import random

def mostrar_opciones():
    print("Elige una opción:")
    print("1 - Piedra")
    print("2 - Papel")
    print("3 - Tijera")

def obtener_eleccion_jugador():
    while True:
        opcion = input("Introduce el número de tu elección (1, 2 o 3): ")

        if opcion in ["1", "2", "3"]:
            return opcion
        else:
            print("Entrada no válida. Por favor, elige 1, 2 o 3.")


def convertir_numero_a_eleccion(numero):
    if numero == "1":
        return "Piedra"
    elif numero == "2":
        return "Papel"
    elif numero == "3":
        return "Tijera"
    else:
        return None

    def mostrar_eleccion_computadora(eleccion):
     print("La computadora ha elegido:", eleccion)

    def generar_eleccion_computadora():
     numero = random.randint(1, 3)
    
    if numero == 1:
        return "Piedra"
    elif numero == 2:
        return "Papel"
    else:
        return "Tijera"

def determinar_ganador(jugador, computadora):
    if jugador == computadora:
        return "Empate"

    if jugador == "Piedra" and computadora == "Tijera":
        return "Jugador"
    elif jugador == "Papel" and computadora == "Piedra":
        return "Jugador"
    elif jugador == "Tijera" and computadora == "Papel":
        return "Jugador"
    else:
        return "Computadora"

def determinar_ganador(jugador, computadora):
    # Si ambos eligen lo mismo → empate
    if jugador == computadora:
        return "Empate"

    # Casos donde gana el jugador
    if jugador == "Piedra" and computadora == "Tijera":
        return "Jugador"
    elif jugador == "Tijera" and computadora == "Papel":
        return "Jugador"
    elif jugador == "Papel" and computadora == "Piedra":
        return "Jugador"

    # Si no es empate ni gana el jugador → gana la computadora
    return "Computadora"

def resultado_ronda(ganador):
    if ganador == "Jugador":
        return "Victoria"
    elif ganador == "Computadora":
        return "Derrota"
    else:
        return "Empate"
    
def mostrar_resultado(resultado):
    print("Resultado de la ronda:", resultado)


