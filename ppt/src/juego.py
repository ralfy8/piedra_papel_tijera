import random
import os

# ---------------------------------------------------------
# Pantalla de bienvenida
# ---------------------------------------------------------
def mostrar_bienvenida():
    print("======================================")
    print("      🎮  PIEDRA - PAPEL - TIJERA 🎮")
    print("======================================")
    print("\nReglas del juego:")
    print(" - Piedra gana a Tijera")
    print(" - Tijera gana a Papel")
    print(" - Papel gana a Piedra")
    print(" - Si ambos eligen lo mismo, es un empate\n")
    print("¡Que comience el juego!\n")


# ---------------------------------------------------------
# Mostrar opciones al jugador
# ---------------------------------------------------------
def mostrar_opciones():
    print("Elige una opción:")
    print("1 - Piedra")
    print("2 - Papel")
    print("3 - Tijera")


# ---------------------------------------------------------
# Obtener elección del jugador con validación y try-except
# ---------------------------------------------------------
def obtener_eleccion_jugador():
    while True:
        opcion = input("Introduce el número de tu elección (1, 2 o 3): ")

        try:
            numero = int(opcion)
        except ValueError:
            print("❌ Error: debes escribir un número, no letras.")
            continue

        if numero in [1, 2, 3]:
            return str(numero)
        else:
            print("❌ Error: elige solo 1, 2 o 3.")


# ---------------------------------------------------------
# Convertir número a texto
# ---------------------------------------------------------
def convertir_numero_a_eleccion(numero):
    if numero == "1":
        return "Piedra"
    elif numero == "2":
        return "Papel"
    elif numero == "3":
        return "Tijera"
    else:
        return None


# ---------------------------------------------------------
# Elección aleatoria de la computadora
# ---------------------------------------------------------
def generar_eleccion_computadora():
    numero = random.randint(1, 3)

    if numero == 1:
        return "Piedra"
    elif numero == 2:
        return "Papel"
    else:
        return "Tijera"


# ---------------------------------------------------------
# Mostrar elección de la computadora
# ---------------------------------------------------------
def mostrar_eleccion_computadora(eleccion):
    print("La computadora ha elegido:", eleccion)


# ---------------------------------------------------------
# Determinar ganador según las reglas del juego
# ---------------------------------------------------------
def determinar_ganador(jugador, computadora):
    if jugador == computadora:
        return "Empate"

    if jugador == "Piedra" and computadora == "Tijera":
        return "Jugador"
    elif jugador == "Tijera" and computadora == "Papel":
        return "Jugador"
    elif jugador == "Papel" and computadora == "Piedra":
        return "Jugador"

    return "Computadora"


# ---------------------------------------------------------
# Convertir ganador en texto de resultado
# ---------------------------------------------------------
def resultado_ronda(ganador):
    if ganador == "Jugador":
        return "Victoria"
    elif ganador == "Computadora":
        return "Derrota"
    else:
        return "Empate"


# ---------------------------------------------------------
# Mostrar resultado por pantalla
# ---------------------------------------------------------
def mostrar_resultado(resultado):
    print("Resultado de la ronda:", resultado)


# ---------------------------------------------------------
# Función principal del juego con rondas infinitas
# ---------------------------------------------------------
def jugar():
    mostrar_bienvenida()

    victorias = 0
    derrotas = 0
    empates = 0
    ronda = 1

    while True:
        os.system('cls' if os.name == 'nt' else 'clear')  # ← limpiar pantalla
        print(f"===== Ronda {ronda} =====")

        mostrar_opciones()
        opcion_jugador = obtener_eleccion_jugador()
        jugador = convertir_numero_a_eleccion(opcion_jugador)

        computadora = generar_eleccion_computadora()
        mostrar_eleccion_computadora(computadora)

        ganador = determinar_ganador(jugador, computadora)
        resultado = resultado_ronda(ganador)
        mostrar_resultado(resultado)

        # Actualizar marcador
        if resultado == "Victoria":
            victorias += 1
        elif resultado == "Derrota":
            derrotas += 1
        else:
            empates += 1

        # Mostrar marcador actual
        print("\n--- Marcador ---")
        print("Victorias:", victorias)
        print("Derrotas:", derrotas)
        print("Empates:", empates)
        print("----------------\n")

        # Preguntar si quiere seguir jugando
        seguir = input("¿Quieres jugar otra ronda? (s/n): ").lower()
        if seguir != "s":
            print("Gracias por jugar. ¡Hasta la próxima!")
            break

        ronda += 1


# ---------------------------------------------------------
# Ejecutar el juego
# ---------------------------------------------------------
jugar()



