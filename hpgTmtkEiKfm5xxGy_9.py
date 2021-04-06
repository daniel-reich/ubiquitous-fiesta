
def paths(x, y):
    if x == 0 or y == 0:
        return 1
    M = [[0 for _ in range(x+1)] for __ in range(y+1)]
    M[0] = [1] * (x+1)
    for row in range(y+1):
        M[row][0] = 1
    for row in range(1, y+1):
        for col in range(1, x+1):
            M[row][col] = M[row-1][col] + M[row][col-1]
    return M[-1][-1]

