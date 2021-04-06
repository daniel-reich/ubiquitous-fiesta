
def tic_tac_toe(board):
    if board[0][0]==board[0][1]==board[0][2] or board[0][0]==board[1][0]==board[2][0] or board[0][0]==board[1][1]==board[2][2] :
        return board[0][0]
    elif board[1][0]==board[1][1]==board[1][2]:
        return board[1][0]
    elif board[2][0]==board[2][1]==board[2][2] or board[2][0]==board[1][1]==board[0][2]:
        return board[2][0]
    elif board[0][1]==board[1][1]==board[2][1]:
        return board[0][1]
    else:
        return 'Draw'

