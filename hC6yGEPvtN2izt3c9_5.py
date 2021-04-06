
def is_mini_sudoku(square):
  a,b,c = square
  return sorted(a+b+c) == [1,2,3,4,5,6,7,8,9]

