
def minesweeper_numbers(board):
    size = len(board)
    arr = [['']*size for _ in range(size)]
    board = [[0]*(size+2)] + [[0]+i+[0] for i in board] + [[0]*(size+2)]
​
    for i in range(1, size + 1):
        for j in range(1, size + 1):
            if board[i][j] == 1:
                arr[i-1][j-1] = 9
            else:
                up = board[i-1][j-1:j+2]
                mid = board[i][j-1:j+2]
                low = board[i+1][j-1:j+2]
                arr[i-1][j-1] = sum(up + mid + low)
    return arr

