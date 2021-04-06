
def is_mini_sudoku(square):
  square=[i for x in square for i in x]
  return sorted(square)==[1,2,3,4,5,6,7,8,9]

