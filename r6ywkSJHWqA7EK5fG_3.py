
def printgrid(rows, cols):
    res = [[] for _ in range(rows)]
    r = 0
    for i in range(1, rows * cols + 1):
        res[r].append(i)
        if r == rows - 1:
            r = 0
        else:
            r += 1
    return res

