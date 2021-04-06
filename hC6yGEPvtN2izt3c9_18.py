
def is_mini_sudoku(square):
  return {i for row in square for i in row} == set(range(1, 10))

