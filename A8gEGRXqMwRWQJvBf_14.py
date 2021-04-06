
def tic_tac_toe(board):
    for x in range (3):
        if board[x][0] == board[x][1] == board[x][2]:
            return board[x][0]
        if board[0][x] == board[1][x] == board[2][x]:
            return board[0][x]
    if board[x][x] == board[x-1][x-1] == board[x-2][x-2]:
        return board[x][x]
    if board[x][x-2] == board[x-1][x-1] == board[x-2][x]:
        return board[x][x-2]
    return "Draw"

