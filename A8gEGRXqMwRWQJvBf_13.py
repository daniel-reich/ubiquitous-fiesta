
def tic_tac_toe(board):
    combos = []
    for i in range(3):
        combos.append([x[i] for x in board])
        combos.append(board[i])
    combos.append([board[0][0], board[1][1], board[2][2]])
    combos.append([board[0][2], board[1][1], board[2][0]])
    
    winner = 'Draw'
    for combo in combos:
        if (combo[0]==combo[1]) & (combo[1]==combo[2]):
            winner = combo[0]
            break
    return winner

