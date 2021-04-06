
def printgrid(rows, cols):
  return [[c*rows+r for c in range(cols)] for r in range(1, rows+1)]

