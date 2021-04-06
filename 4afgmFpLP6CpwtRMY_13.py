
def sudoku_validator(board):
    valid = {1,2,3,4,5,6,7,8,9}
    zipped = [list(x) for x in zip(*board)]
    if any(set(valid).difference(x) for x in board):
        return False
    if any(set(valid).difference(x) for x in zipped):
        return False
    threes = [board[x:x+3] for x in range(0,8,3)]
    threes = sum([list(zip(*x))for x in threes], [])
    threes = [sum(threes[x:x+3], ()) for x in range(0,len(threes),3)]
    if any(set(valid).difference(x) for x in threes):
        return False
    return True

