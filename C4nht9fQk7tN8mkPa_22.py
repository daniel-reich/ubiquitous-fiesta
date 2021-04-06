
def ok_coords(x, y):
    return True if x >= 0 and x <= 7 and y >= 0 and y <= 7 else False
​
def cannot_capture(board):
    check = lambda r, c: board[r][c] == 1
    tests = [(2,1),(2,-1),(-2,1),(-2,-1),(1,2),(1,-2),(-1,2),(-1,-2)]
    capture = False
    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col]:
                results = []
                for x, y in [ (row+a, col+b) for a, b in tests]:
                    if ok_coords(x, y):
                        results += [check(x, y)]
                if any(results):
                    return False
    return True

