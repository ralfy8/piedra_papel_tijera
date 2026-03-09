El juego implementará las reglas clásicas (Piedra vence a Tijera · Tijera vence a Papel · Papel vence a 
Piedra), un sistema de puntuación por partidas, estadísticas de la sesión y una interfaz de usuario clara en la 
terminal. 
Ahi tienes la idea principal de mi proyecto.
DE MOMENTO NO GENERES CODIGO

no me generes codigo aun.
quiero que todo el codigo que generes, sea sencillo y simple de entender para cualquier programador basico.
te voy a ir dando las funciones de poco en poco, aqui tienes la primera

Crear función que muestre las opciones al jugador (1=Piedra, 2=Papel, 3=Tijera)

Capturar la elección del jugador por teclado

Convertir el número introducido al nombre de la elección

¿Cómo capturo la entrada del usuario en Python con input()?añadelo a mi codigo

Importar el módulo random

Crear función que genere una elección aleatoria para la computadora

Mostrar por pantalla qué ha elegido la computadora

Crear función que compare la elección del jugador con la de la computadora

Implementar la lógica completa: Piedra vence Tijera, Tijera vence Papel, Papel vence Piedra

Devolver el resultado de la ronda: Victoria, Derrota o Empate

ahora 
● Mostrar el resultado por pantalla con un mensaje claro

Validar que el jugador introduzca solo los valores 1, 2 o 3

● Mostrar un mensaje de error si la entrada no es válida

Pedir de nuevo la entrada hasta que sea correcta (bucle while)

Manejar errores de tipo con try-except (por si el usuario escribe letras)

Crear variables para llevar el marcador: victorias, derrotas y empates

// INCISO //

Aqui la IA me sugerio cear una funcion llamada jugar() completa, que añadiria bucles para jugar varisa rondas y al final me mostraria el marcador final.
Cosa que le dije que me lo realizase.

Actualizar el marcador después de cada ronda

Mostrar el marcador actual al final de cada ronda

Preguntar al jugador cuántas rondas quiere jugar al inicio de la partida

no quiero que me pregunte cuantas rondas quiero jugar, si no que hasta que yo no le diga que no quiero jugar mas, siga sacando rondas una vez acaben

Validar que el número de rondas sea un entero positivo

Implementar el bucle principal del juego para gestionar todas las rondas

Mostrar el número de ronda actual (ej: Ronda 2 de 5)

Crear pantalla de bienvenida con el título del juego y las reglas

Limpiar la pantalla entre rondas usando os.system('cls' o 'clear')

pero que cuando lo ejecute por primerza vez, me salga el panel de bienvenida

Mostrar un resumen completo al final de la partida (victorias, derrotas, empates)

Calcular y mostrar el porcentaje de victorias del jugador 
● Determinar y mostrar al ganador final de la partida

ahora, que cuando me diga de si quiero seguir jugando, solo acepte "s" o "n" da igual que sea mayuscula o minuscula, pero que SOLAMENTE acepte eso.

Agregar docstrings a todas las funciones siguiendo el estilo de Python

Refactorizar el código para eliminar repeticiones (principio DRY) 

Añadir opción de jugar otra partida al terminar sin cerrar el programa 

Probar todos los casos edge: entrada vacía, letras, números negativos 

REFLEXIONES FINALES.

El Codigo, al final ha resultado exitoso, todo esto gracias a darle los promts correctos, explicados y sencillos (concretos)
Lo unico que me ha dado fallos ha sido el tenerlo dentro de la carpeta "src/" pero gracias a la IA este problema fue resulto. Aunque yo le haya dado los promts el codigo sigue teniendo fallos, los cuales han sido corregidos mediante pruebas, 
ej: En la opcion de continuar s/n si yo le ponia cualquier cosa que no fuese n o s, lo detectaba como acabar la partida, cosa que he tenido que corregir.
Ej2: cuando le mande la funcion de que me haga clear entre ronda y ronda, al ejecutar el codigo no me aparecia el menu de bienvenida, otra cosa que he tenido que corregir.
En resumen, que aunque la IA sea una muy buena herramienta para programar, siempre tendra algun fallo ( igual con promts mucho mas detallados y extensos, se puede corregir) y necesita ser supervisada por una persona con conocimientos de programacion aunque sean basicos. Porque le puedes pedir a la IA que te explique de manera sencilla el codigo que ha generado paso por pasa. Y por estas cosas, yo creo que la IA nunca podra sustituir a un programador. 