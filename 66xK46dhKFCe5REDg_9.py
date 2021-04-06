
def x_and_o(board):
    board = [i.split('|') for i in board]
​
    for r in range(3):
        for c in range(3):
            if board[r][c] == ' ':
                board[r][c] = 'X'
                row = board[r]
                col = [board[0][c], board[1][c], board[2][c]]
                d_1 = [board[0][0], board[1][1], board[2][2]]
                d_2 = [board[0][2], board[1][1], board[2][0]]
                if any(i == ['X', 'X', 'X'] for i in (row, col, d_1, d_2)):
                    return [r+1, c+1]
                board[r][c] = ' '
    return False

