
def is_wristband(lst):
  h = len(lst)
  w = len(lst[0])
  if all(row.count(row[0]) == len(row) for row in lst):
    return True
  if all(col.count(col[0]) == len(col) for col in zip(*lst)):
    return True
    
  left = right = True
  for i in range(h):
    for j in range(w):
      if i > 0 and j > 0 and lst[i][j] != lst[i-1][j-1]:
        left = False
      if i > 0 and j < w-1 and lst[i][j] != lst[i-1][j+1]:
        right = False
    
  return left or right

