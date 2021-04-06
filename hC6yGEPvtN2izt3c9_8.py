
def is_mini_sudoku(square):
  s=[]
  for i in square:
    s+=i
  if 0 in set(s):
    return False
  return len(set(s))==9

