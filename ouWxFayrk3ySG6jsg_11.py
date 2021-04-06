
def check_triple(triple):
    # check whether a triple of values is a winning position:
    return len(set(triple)) == 1 and triple[0] != 's'
​
def isSolved(board):
    # first check if there's a winner:
    # check rows:
    for row in board:
        if check_triple(row):
            return row[0]
    # check columns:
    for col in range(3):
        column = [board[row][col] for row in range(3)]
        if check_triple(column):
            return column[0]
    # check diagonals:
    if check_triple([board[i][i] for i in range(3)]):
        return board[0][0]
    if check_triple([board[i][2-i] for i in range(3)]):
        return board[2][0]
    #
    # no winner:
    return "Draw"
​
def who_won(board):
    return isSolved(board)

