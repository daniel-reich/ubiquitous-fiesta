
def cap(board,i,j):
    return board[i-2][j-1] or board[i-2][j+1] or board[i-1][j-2] or board[i-1][j+2] or board[i+1][j-2] or board[i+1][j+2] or board[i+2][j-1] or board[i+2][j+1]
    
def cannot_capture(board):
    new_board = [[board[i-2][j-2] if i in range(2,10) and j in range(2,10) else 0 for j in range(12)] for i in range(12)]
    for i in range(2,10):
        for j in range(2,10):
            if new_board[i][j] == 1 and cap(new_board,i,j):
                return False
    return True

