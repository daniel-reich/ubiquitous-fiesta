
def sudoku_validator(x):
  import numpy as np
  matrix = np.array(x)
  box = []
  check_box = []
  for i in range(9):
    if sorted(matrix[i, :]) != [1,2,3,4,5,6,7,8,9]:  
      print('row error')
      return False
    if sorted(matrix[:, i]) != [1,2,3,4,5,6,7,8,9]:  
      print('column error')
      return False
  for row in range(0, 9, 3):
    for col in range(0, 9, 3):
      box = matrix[row : row + 3, col : col + 3]   
      for number in range(1, 10):
        check_box.append(np.count_nonzero(box == number))
      if check_box != [1]*9:
        return False
      else:
        check_box = []
        box = []
  return True

