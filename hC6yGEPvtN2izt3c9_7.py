
def is_mini_sudoku(square):
  l=[]
  for i in square:
    for j in i:
      l.append(j)
  for k in l:
    if k==0 or l.count(k)>1:
      return False
  return True

