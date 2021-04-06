
def printgrid(rows, cols):
  return [[j+1 + i*rows for i in range(cols)] for j in range(rows)]

