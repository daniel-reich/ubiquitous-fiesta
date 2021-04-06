
def tic_tac_toe(board):
    d1,d2 = [],[]
    for i in range(3):
        col = [board[0][i],board[1][i],board[2][i]]
        if board[i].count('X')==3 or col.count('X')==3:return 'X'
        if board[i].count('O')==3 or col.count('O')==3:return 'O'
        d1 += [board[i][i]]
        d2 += [board[i][2-i]]
    if d1.count('X')==3:return 'X' 
    if d1.count('O')==3:return 'O'  
    return 'Draw'

