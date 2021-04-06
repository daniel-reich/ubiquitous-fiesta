
def tic_tac_toe(board):
    """Tic Tac Toe"""
    a, b, c = board
​
    # Rows and columns
    for i in range(3):
        if a[i] == b[i] == c[i]:
            return a[i]
        elif board[i][0] == board[i][1] == board[i][2]:
            return board[i][0]
    
    # Diagonals
    if a[0] == b[1] == c[2]:
        return a[0]
    elif a[2] == b[1] == c[0]:
        return a[2]
    else:
        return "Draw"

