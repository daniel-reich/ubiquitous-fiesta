
def tic_tac_toe(inputs):
    for i in range(0, 3):
        if all(inputs[i][j] == inputs[i][0] for j in range(1, 3)):
            return "Player 1 wins" if inputs[i][0] == "X" else "Player 2 wins"
    for j in range(0, 3):
        if all(inputs[i][j] == inputs[0][j] for i in range(1, 3)):
            return "Player 1 wins" if inputs[i][0] == "X" else "Player 2 wins"
    if all(inputs[i][i] == inputs[0][0] for i in range(1, 3)):
        return "Player 1 wins" if inputs[0][0] == "X" else "Player 2 wins"
    if all(inputs[i][2-i] == inputs[0][2] for i in range(1, 3)):
        return "Player 1 wins" if inputs[0][2] == "X" else "Player 2 wins"
    return "It's a Tie"

