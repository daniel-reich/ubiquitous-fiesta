
def printgrid(rows, cols):
    return [[1+row+col*rows for col in range(cols)] for row in range(rows)]

