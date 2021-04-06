
def minesweeper_numbers(board):
    board2= [[i for i in j] for j in board]
    for row in range(len(board)):
        for col in range(len(board[0])):
            if board[row][col] == 1:
                board2[row][col] = 9
            else:
                board2[row][col] = check(board,row,col)
    return board2
​
def check(board,row,col):
    around = [1,0,-1]
    count = 0
    for i in around:
        for j in around:
            if 0 <= row + i < len(board) and 0 <= col + j < len(board[0]):
                if board[row + i][col + j] == 1:
                    count += 1  
    return count

