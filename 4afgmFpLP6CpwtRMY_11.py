
from itertools import product
​
def row_check(mtx):
  for i in mtx:
    if sorted(i) != [a for a in range(1,10)]:
      return False
  return True
  
  
def sudoku_validator(x):
  y = [[x[a][b] for a in range(9)] for b in range(9)[::-1]]
  R = range(3)
  z = [[x[3*j[0]+i[0]][3*j[1]+i[1]] for i in product(R,R)] for j in product(R,R)]
  if row_check(x) == True and row_check(y) == True and row_check(z) == True:
    return True
  return False

