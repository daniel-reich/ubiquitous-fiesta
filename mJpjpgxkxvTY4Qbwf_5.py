
def bingo_check(board):
    line = lambda arr: any(set(i) == {'x'} for i in arr)
    diag = lambda arr: all(arr[i][i] == 'x' for i in range(5))
    
    if line(board) or diag(board):
        return True
    board = [i[::-1] for i in zip(*board)]
    if line(board) or diag(board):
        return True
    return False

