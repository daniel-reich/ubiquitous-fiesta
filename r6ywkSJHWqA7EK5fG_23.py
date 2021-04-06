
def printgrid(rows, cols):
    sol = []
    for num in range(1, rows + 1):
        sol.append([num + rows*n for n in range(cols)])
    return sol

