
def tic_tac_toe(board):
    f = lambda *a: board[a[0]][a[1]] == board[a[2]][a[3]] == board[a[4]][a[5]]
​
    horizontal = [(0, 0, 0, 1, 0, 2), (1, 0, 1, 1, 1, 2), (2, 0, 2, 1, 2, 2)]
    vertical = [(0, 0, 1, 0, 2, 0), (0, 1, 1, 1, 2, 1), (0, 2, 1, 2, 2, 2)]
    diagonal = [(0, 0, 1, 1, 2, 2), (-1, -1, -2, -2, -3, -3)]
    
    for direction in horizontal + vertical + diagonal:
        if f(*direction):
            return board[direction[0]][direction[1]]
​
    return "Draw"

