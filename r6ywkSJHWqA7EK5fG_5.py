
def printgrid(rows, cols):
  A=list(range(1, rows*cols+1))
  B=[A[i:i+rows] for i in range(0, len(A), rows)]
  return [list(x) for x in zip(*B)]

