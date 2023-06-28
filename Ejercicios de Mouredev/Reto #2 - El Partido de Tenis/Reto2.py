""" 
/*
 * Escribe un programa que muestre cómo transcurre un juego de tenis y quién lo ha ganado.
 * El programa recibirá una secuencia formada por "P1" (Player 1) o "P2" (Player 2), según quien
 * gane cada punto del juego.
 * 
 * - Las puntuaciones de un juego son "Love" (cero), 15, 30, 40, "Deuce" (empate), ventaja.
 * - Ante la secuencia [P1, P1, P2, P2, P1, P2, P1, P1], el programa mostraría lo siguiente:
 *   15 - Love
 *   30 - Love
 *   30 - 15
 *   30 - 30
 *   40 - 30
 *   Deuce
 *   Ventaja P1
 *   Ha ganado el P1
 * - Si quieres, puedes controlar errores en la entrada de datos.   
 * - Consulta las reglas del juego si tienes dudas sobre el sistema de puntos.   
 */
"""

def game_score(sequence):
    scores = {
        0: "Love",
        15: "15",
        30: "30",
        40: "40"
    }

    p1_score = 0
    p2_score = 0

    for point in sequence:
        if point == "P1":
            p1_score += 1
        elif point == "P2":
            p2_score += 1

        if p1_score >= 3 and p2_score >= 3:
            if p1_score == p2_score:
                print("Deuce")
            elif p1_score == p2_score + 1:
                print("Ventaja P1")
            elif p2_score == p1_score + 1:
                print("Ventaja P2")
            elif p1_score >= 4 and p1_score - p2_score >= 2:
                print("Ha ganado el P1")
                return
            elif p2_score >= 4 and p2_score - p1_score >= 2:
                print("Ha ganado el P2")
                return
        else:
            print(scores.get(p1_score, "Invalid score"), "-", scores.get(p2_score, "Invalid score"))

sequence = ["P1", "P1", "P2", "P2", "P1", "P2", "P1", "P1"]
game_score(sequence)

'''
Se define una función llamada game_score que toma una lista llamada sequence como entrada. Esta lista contiene la secuencia de puntos del juego de tenis.

Se define un diccionario llamado scores que mapea los valores numéricos de los puntos a sus representaciones en el juego de tenis. Por ejemplo, el valor 0 se mapea a "Love", 15 a "15", 30 a "30" y 40 a "40".

Se inicializan las variables p1_score y p2_score con un valor de 0. Estas variables llevarán el registro de los puntajes de los jugadores 1 y 2, respectivamente.

Se recorre la lista sequence utilizando un bucle for para procesar cada punto del juego.

Dentro del bucle, se verifica si el punto es para el jugador 1 ("P1") o para el jugador 2 ("P2"). Si es para el jugador 1, se incrementa su puntaje en 1; si es para el jugador 2, se incrementa su puntaje en 1.

A continuación, se realizan varias comprobaciones para determinar el estado del juego y quién ha ganado.

Si tanto el puntaje del jugador 1 como el del jugador 2 son iguales o superiores a 3, se verifica si hay un empate ("Deuce") o si alguno de los jugadores tiene una ventaja de un punto sobre el otro.

Si el puntaje del jugador 1 es mayor o igual a 4 y tiene al menos dos puntos de ventaja sobre el jugador 2, se imprime "Ha ganado el P1" y la función retorna, finalizando el juego.

Si el puntaje del jugador 2 es mayor o igual a 4 y tiene al menos dos puntos de ventaja sobre el jugador 1, se imprime "Ha ganado el P2" y la función retorna, finalizando el juego.

Si ninguna de las condiciones anteriores se cumple, se imprime el puntaje actual de ambos jugadores utilizando el diccionario scores para obtener las representaciones correspondientes.

Después de salir del bucle, el juego ha terminado y la función también termina.

Finalmente, se crea una lista sequence con una secuencia de puntos de ejemplo y se llama a la función game_score pasando esa lista como argumento.

El resultado será la impresión de los puntajes y el desarrollo del juego en la consola, incluyendo quién ha ganado al final.
'''

