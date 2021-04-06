
def tic_tac_toe(board):
    c = 0
    if board[0][0] == board[1][1] and board[2][2] == board[1][1]:
        c += 1
        return board[0][0]
    if board[0][2] == board[1][1] and board[1][1] == board[2][0]:
        c += 1
        return board[1][1]
    for j in range(3) :
        if board[j][0] == board[j][1] and board[j][1] == board[j][2] :
            c += 1
            return board[j][0]
    for i in range(3) :
        if board[0][i] == board[1][i] and board[2][i] == board[1][i] :
            c += 1
            return board[0][i]
    if c == 0 :
        return 'Draw'

