
def tic_tac_toe(board):
    f = 0
        
    for i in range(len(board)):
        if board[i][0] == board[i][1] == board[i][2]:
            f = 1
            return board[i][0]
    for i in range(3):
        if board[0][i] == board[1][i] == board[2][i]:
            f = 1
            return board[0][i]
    if board[0][0] == board[1][1]== board[2][2]:
        f = 1
        return board[1][1]
    if board[0][2] == board[1][1]== board[2][0]:
        f = 1
        return board[1][1]
    if f ==0:
        return "Draw"

