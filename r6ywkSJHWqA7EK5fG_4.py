
def printgrid(rows, cols):
    arr = []
    for r in range(1, rows+1):
        row = []
        for n in range(r, rows*cols + 1, rows):
            row.append(n)
        arr.append(row)
    return arr

