
def is_mini_sudoku(square):
  s = '123456789'
  return all(i in str(square) for i in s)

