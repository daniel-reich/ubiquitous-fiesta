
def snakefill(n):
  total_grid = n*n
  current_grid = 1
  i = 0
  while current_grid + 2**i <= total_grid:
    current_grid += 2**i
    i += 1
  return i

