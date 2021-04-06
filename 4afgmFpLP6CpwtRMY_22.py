
def sudoku_validator(arr):
  rows = [len(set(i)) for i in arr]
  cols = [len(set(i)) for i in zip(*arr)]
  squares = [len(set(arr[r][c] for r in range(i//3*3, i//3*3+3) for c in range(i%3*3, i%3*3+3))) for i in range(9)]
  return set(rows + cols + squares) == {9}

