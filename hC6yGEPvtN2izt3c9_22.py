
def is_mini_sudoku(square):
  return sorted(i for x in square for i in x) == list(range(1,10))

