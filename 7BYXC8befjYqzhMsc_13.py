
import math
​
def isSymmetric(pattern, axis):
  rows = len(pattern)
  cols = len(pattern[0])
  mid = 0
  
  if axis == 0:
    mid = math.ceil(rows / 2)
    rows //= 2
  else:
    mid = math.ceil(cols / 2)
    cols //= 2    
    
  for row in range(rows):
    for col in range(cols):
      adjusted_row = row
      adjusted_col = col
      
      if axis == 0:
        adjusted_row += mid
      else:
        adjusted_col += mid
      
      if not pattern[row][col] == pattern[adjusted_row][adjusted_col]:
        return False
​
  return True
​
def classify_rug(pattern):
  horizontally_symmetric = isSymmetric(pattern, 0)
  vertically_symmetric = isSymmetric(pattern, 1)
  
  if horizontally_symmetric and vertically_symmetric:
    return "perfect"
  if horizontally_symmetric:
    return "horizontally symmetric"
  if vertically_symmetric:
    return "vertically symmetric"
  else:
    return "imperfect"

