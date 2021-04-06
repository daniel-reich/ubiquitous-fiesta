
def printgrid(rows, cols):
  return [[i + j for i in range(1, rows * (cols - 1) + 2, rows)] for j in range(0, rows)]

