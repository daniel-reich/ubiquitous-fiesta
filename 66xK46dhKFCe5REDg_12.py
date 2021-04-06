
import copy
​
def check_board(board, symbol):
    win_pos = [symbol] * 3
    for row in board:
        if row == win_pos:
            return True
    if [board[i][i] for i in range(3)] == win_pos or \
       [board[2-i][i] for i in range(3)] == win_pos:
        return True
    for c in range(3):
        col = [board[r][c] for r in range(3)]
        if col == win_pos:
            return True
    return False
​
def x_and_o(board):
    for i in range(3):
        board[i] = board[i].split('|')
    for row in range(3):
        for col in range(3):
            if board[row][col] == ' ':
                new_board = copy.deepcopy(board)
                new_board[row][col] = 'X'
                if check_board(new_board, 'X'):
                    return [row + 1, col + 1]
    return False

