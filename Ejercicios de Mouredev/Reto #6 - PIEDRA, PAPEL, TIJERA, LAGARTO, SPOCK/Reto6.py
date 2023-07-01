# Crea un programa que calcule quien gana más partidas al piedra,
# papel, tijera, lagarto, spock.
# - El resultado puede ser: "Player 1", "Player 2", "Tie" (empate)
# - La función recibe un listado que contiene pares, representando cada jugada.
# - El par puede contener combinaciones de "🗿" (piedra), "📄" (papel),
#   "✂️" (tijera), "🦎" (lagarto) o "🖖" (spock).
# - Ejemplo. Entrada: [("🗿","✂️"), ("✂️","🗿"), ("📄","✂️")]. Resultado: "Player 2".
# - Debes buscar información sobre cómo se juega con estas 5 posibilidades.

def jugar_piedra_papel_tijera_lagarto_spock(partidas):
    reglas = {
        ("🗿", "✂️"): "Player 1",
        ("✂️", "🗿"): "Player 2",
        ("🗿", "🦎"): "Player 1",
        ("🦎", "🗿"): "Player 2",
        ("📄", "🗿"): "Player 1",
        ("🗿", "📄"): "Player 2",
        ("📄", "✂️"): "Player 1",
        ("✂️", "📄"): "Player 2",
        ("✂️", "🦎"): "Player 1",
        ("🦎", "✂️"): "Player 2",
        ("🦎", "📄"): "Player 1",
        ("📄", "🦎"): "Player 2",
        ("🖖", "✂️"): "Player 1",
        ("✂️", "🖖"): "Player 2",
        ("🖖", "🗿"): "Player 1",
        ("🗿", "🖖"): "Player 2",
        ("🖖", "📄"): "Player 1",
        ("📄", "🖖"): "Player 2"
    }

    puntuaciones = {"Player 1": 0, "Player 2": 0}

    for jugada in partidas:
        if jugada in reglas:
            ganador = reglas[jugada]
            puntuaciones[ganador] += 1
        else:
            print("Jugada inválida:", jugada)

    if puntuaciones["Player 1"] > puntuaciones["Player 2"]:
        return "Player 1"
    elif puntuaciones["Player 1"] < puntuaciones["Player 2"]:
        return "Player 2"
    else:
        return "Tie"

partidas = [("🗿","✂️"), ("✂️","🗿"), ("📄","✂️")]
resultado = jugar_piedra_papel_tijera_lagarto_spock(partidas)
print("El ganador es:", resultado)