
def is_mini_sudoku(square):
  mn = 9
  mx = 0
  r = set()
  for i in range(0,len(square)):
    for j in range(0,len(square[0])):
      p = square[i][j]
      r.add(p)
      if(p < mn):
        mn = p
      if(p > mx):
        mx = p
  if((mx != 9) or (mn != 1)):
    return bool(0)
  k = list(r)
  if(len(k) != 9):
    return bool(0)
  return bool(1)

