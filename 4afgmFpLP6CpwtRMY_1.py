
def sudoku_validator(r):
  c = [[r[i][j] for i in range (9)] for j in range (9)]
  s = [r[i*3][j*3:(j+1)*3]+r[i*3+1][j*3:(j+1)*3]+r[i*3+2][j*3:(j+1)*3] for j in range (3) for i in range (3)]
  for i in r+c+s:
    for j in range (1,10):
      if j not in i:
        return False
  return True

