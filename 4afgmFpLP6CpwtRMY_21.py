
def sudoku_validator(s):
  for i in range(3):
    for j in range(3):
      opt = []
      if len(set(s[i*3+j]))!=9: return False
      for k in range(9):opt+=[s[k][i*3+j]]
      if len(set(opt))!=9: return False
      x, y = i*3, j*3
      opt = s[y][x:x+3]+s[y+1][x:x+3]+s[y+2][x:x+3]
      if len(set(opt))!=9:return False
  return True

