
def is_mini_sudoku(square):
  return sorted(sum(square, [])) == list(range(1, 10))

