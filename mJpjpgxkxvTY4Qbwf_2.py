
def bingo_check(board):
    return row_check(board) or diag_check(board) or tf_check(board) 
    
def row_check(board):
    for row in board:
        check = 0
        for col in row:
            if col == 'x':
                check += 1
                if check == 5:
                    return True
    return False
​
def diag_check(board):
    check = 0
    for row in range(len(board)):
        for col in range(len(board[row])):
            if row == col and board[row][col] == 'x':
                check += 1
    return check == 5
​
def tf_check(board):
    trans = [[],[],[],[],[]]
    flip = [[],[],[],[],[]]
    for row in range(len(board)):
        for col in range(len(board[row])):
            trans[col].append(board[row][col])
            flip[4-row].append(board[row][col])
    return row_check(trans) or diag_check(flip)

