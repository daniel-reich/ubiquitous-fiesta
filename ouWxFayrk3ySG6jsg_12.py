
def who_won(board):
    a = check(board)
    b = check(zip(*board))
    c = check([
                [board[0][0], board[1][1], board[2][2]], 
                [board[0][2], board[1][1], board[2][0]]
                ])
    return a or b or c
    
def check(x):
    for i in x:
        if len(set(i)) == 1:
            return list(set(i))[0]

