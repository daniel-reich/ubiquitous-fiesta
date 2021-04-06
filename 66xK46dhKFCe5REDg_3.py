
def transpose(lst):
    return [list(x) for x in zip(*lst)]
​
​
def check_win(board) -> bool:
    for row, column in zip(board, transpose(board)):
        if row.count('X') == 3 or column.count('X') == 3:
            return True
​
    diagonal1 = [board[0][0], board[1][1], board[2][2]]
    diagonal2 = [board[0][2], board[1][1], board[2][0]]
    return diagonal1.count('X') == 3 or diagonal2.count('X') == 3
​
​
def x_and_o(board):
    board = [row.split('|') for row in board]
    for i, row in enumerate(board):
        for j, item in enumerate(row):
            temp = [[j for j in i] for i in board]
            temp[i][j] = 'X'
            if item.isspace():
                temp[i][j] = 'X'
                if check_win(temp):
                    return [i+1, j+1]
    else:
        return False

