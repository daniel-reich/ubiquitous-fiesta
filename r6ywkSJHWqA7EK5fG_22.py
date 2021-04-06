
def printgrid(rows, cols):
  return [[j for j in range(i+1,rows*cols+1,rows)] for i in range(0,rows)]

