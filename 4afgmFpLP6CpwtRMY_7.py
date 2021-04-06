
def list_validator(lst):
  for n in range(1,10):
    if n not in lst:
      return False
  return True
  
  
def sudoku_validator(x):
  orizontal = []
  for lst in x:
    orizontal = list_validator(lst)
    if orizontal != True:
      return False
  for n in range(0,9):
    vertical = []
    for lst in x:
      vertical.append(lst[n])
    if list_validator(vertical) != True:
      return False
      
  square_list = [0, 3, 6, 9]
  
  for n in range(0,3):
    squares = []
    for lst in x[square_list[n]:square_list[n+1]]:
      m = 0
      while m < 3:
        squares.append(lst[m])
        m += 1
    if list_validator(squares) != True:
      return False  
      
  for n in range(0,3):
    squares = []
    for lst in x[square_list[n]:square_list[n+1]]:
      m = 3
      while m < 6:
        squares.append(lst[m])
        m += 1
    if list_validator(squares) != True:
      return False
      
  for n in range(0,3):
    squares = []
    for lst in x[square_list[n]:square_list[n+1]]:
      m = 6
      while m < 9:
        squares.append(lst[m])
        m += 1
    if list_validator(squares) != True:
      return False
      
  return True

