
def minesweeper_numbers(board):
​
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == 1:
                board[i][j] = 9
                
    for i in range(len(board)):
        for j in range(len(board[i])):                
            if board[i][j] != 9:
                board[i][j] = sum(1 for l in range(i-1, i+2) for p in range(j-1, j+2) 
                       if 0 <= l < len(board) and 0 <= p < len(board[i]) and board[l][p] == 9)
    return board

