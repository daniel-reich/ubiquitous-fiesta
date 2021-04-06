
def check_board(col, row):
    col_dict = dict(zip(map(chr, range(ord('a'), ord('h')+1)), range(0,8)))
    col_num = col_dict.get(col)
    
    board = [[0 for _ in range(0,8)] for _ in range(8)]
    
    for b_row in range(8):
        for b_col in range(8):
            if b_row == row-1 or b_col == col_num or abs(b_row - (row-1)) == abs(b_col - col_num): 
                board[b_row][b_col] = 1
    board[row-1][col_num] = 0
    return board[::-1]

