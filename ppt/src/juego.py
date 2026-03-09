import random
import os

# ---------------------------------------------------------
# Utilidades generales
# ---------------------------------------------------------
def limpiar_pantalla():
    """Limpia la pantalla de la consola según el sistema operativo."""
    os.system('cls' if os.name == 'nt' else 'clear')


def pedir_confirmacion(mensaje):
    """
    Solicita al usuario una confirmación 's' o 'n'.

    Args:
        mensaje (str): Texto a mostrar al usuario.

    Returns:
        bool: True si el usuario responde 's', False si responde 'n'.
    """
    while True:
        respuesta = input(mensaje).lower()
        if respuesta in ["s", "n"]:
            return respuesta == "s"
        print("❌ Solo se permite 's' o 'n'. Inténtalo de nuevo.")


# ---------------------------------------------------------
# Pantalla de bienvenida
# ---------------------------------------------------------
def mostrar_bienvenida():
    """Muestra la pantalla de bienvenida del juego junto con las reglas."""
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
# Opciones del juego
# ---------------------------------------------------------
def mostrar_opciones():
    """Muestra las opciones disponibles para que el jugador elija."""
    print("Elige una opción:")
    print("1 - Piedra")
    print("2 - Papel")
    print("3 - Tijera")


def obtener_eleccion_jugador():
    """
    Solicita al jugador que introduzca una opción válida (1, 2 o 3).

    Returns:
        str: La opción elegida por el jugador como cadena.
    """
    while True:
        opcion = input("Introduce el número de tu elección (1, 2 o 3): ")

        try:
            numero = int(opcion)
        except ValueError:
            print("❌ Error: debes escribir un número, no letras.")
            continue

        if numero in [1, 2, 3]:
            return str(numero)

        print("❌ Error: elige solo 1, 2 o 3.")


def convertir_numero_a_eleccion(numero):
    """
    Convierte un número en su equivalente textual del juego.

    Args:
        numero (str): "1", "2" o "3".

    Returns:
        str: "Piedra", "Papel" o "Tijera".
    """
    return {"1": "Piedra", "2": "Papel", "3": "Tijera"}.get(numero)


def generar_eleccion_computadora():
    """Genera aleatoriamente la elección de la computadora."""
    return random.choice(["Piedra", "Papel", "Tijera"])


def mostrar_eleccion_computadora(eleccion):
    """Muestra la elección realizada por la computadora."""
    print("La computadora ha elegido:", eleccion)


# ---------------------------------------------------------
# Lógica del juego
# ---------------------------------------------------------
def determinar_ganador(jugador, computadora):
    """
    Determina el ganador de la ronda.

    Args:
        jugador (str)
        computadora (str)

    Returns:
        str: "Jugador", "Computadora" o "Empate".
    """
    if jugador == computadora:
        return "Empate"

    reglas = {
        "Piedra": "Tijera",
        "Tijera": "Papel",
        "Papel": "Piedra"
    }

    return "Jugador" if reglas[jugador] == computadora else "Computadora"


def resultado_ronda(ganador):
    """Convierte el ganador en un texto descriptivo."""
    return {
        "Jugador": "Victoria",
        "Computadora": "Derrota",
        "Empate": "Empate"
    }[ganador]


def mostrar_marcador(victorias, derrotas, empates):
    """Muestra el marcador actual."""
    print("\n--- Marcador ---")
    print("Victorias:", victorias)
    print("Derrotas:", derrotas)
    print("Empates:", empates)
    print("----------------\n")


def mostrar_resumen_final(victorias, derrotas, empates):
    """Muestra el resumen final de la partida."""
    total = victorias + derrotas + empates
    porcentaje = (victorias / total) * 100 if total > 0 else 0

    if victorias > derrotas:
        ganador_final = "Jugador"
    elif derrotas > victorias:
        ganador_final = "Computadora"
    else:
        ganador_final = "Empate"

    print("\n===== RESUMEN FINAL =====")
    print(f"Rondas jugadas: {total}")
    print(f"Victorias: {victorias}")
    print(f"Derrotas: {derrotas}")
    print(f"Empates: {empates}")
    print(f"Porcentaje de victorias: {porcentaje:.2f}%")
    print(f"Ganador final: {ganador_final}")
    print("=========================\n")


# ---------------------------------------------------------
# Bucle principal del juego
# ---------------------------------------------------------
def jugar():
    """Ejecuta una partida completa del juego."""
    victorias = derrotas = empates = 0
    ronda = 1

    while True:
        limpiar_pantalla()
        print(f"===== Ronda {ronda} =====")

        mostrar_opciones()
        jugador = convertir_numero_a_eleccion(obtener_eleccion_jugador())
        computadora = generar_eleccion_computadora()

        mostrar_eleccion_computadora(computadora)

        ganador = determinar_ganador(jugador, computadora)
        resultado = resultado_ronda(ganador)
        print("Resultado de la ronda:", resultado)

        if resultado == "Victoria":
            victorias += 1
        elif resultado == "Derrota":
            derrotas += 1
        else:
            empates += 1

        mostrar_marcador(victorias, derrotas, empates)

        if not pedir_confirmacion("¿Quieres jugar otra ronda? (s/n): "):
            mostrar_resumen_final(victorias, derrotas, empates)
            break

        ronda += 1


# ---------------------------------------------------------
# Bucle principal del programa (NUEVO)
# ---------------------------------------------------------
def main():
    """
    Bucle principal del programa.
    Permite jugar múltiples partidas sin cerrar el programa.
    """
    while True:
        limpiar_pantalla()
        mostrar_bienvenida()
        input("Pulsa ENTER para comenzar...")

        jugar()

        if not pedir_confirmacion("¿Quieres jugar otra partida completa? (s/n): "):
            print("Gracias por jugar. ¡Hasta la próxima!")
            break


# ---------------------------------------------------------
# Ejecutar el programa
# ---------------------------------------------------------
main()

