
def is_mini_sudoku(square):
  return sorted(sum(square,[]))==sorted(range(1,10))

