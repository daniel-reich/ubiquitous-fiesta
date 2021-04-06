
def is_mini_sudoku(square):
  sum = 0
  
  for row in square:
    for element in row:
      if element < 1 or element > 9:
        return False
      sum += element
      
  return sum == 45

