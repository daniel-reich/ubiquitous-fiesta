
def check_board(col, row):
    c = 'abcdefgh'
    cInd = {i:c.index(i) for i in c}
    r,c = 8-row,cInd[col]
    board = [[0 for i in range(8)] for i in range(8)]
    #non diag
    for i in board:
        i[c] = 1 
    for i in range(len(board)):
        board[r][i] = 1
    #c1
    for i in range(1,min([r,7-c])+1):
        board[r-i][c+i] = 1
    #c2
    for i in range(1,min([r,c])+1):
        board[r-i][c-i] = 1
    #c3
    for i in range(1,min([7-r,c])+1):
        board[r+i][c-i] = 1
    #c4
    for i in range(1,min([7-r,7-c])+1):
        board[r+i][c+i] = 1
    board[r][c] = 0
    return board

