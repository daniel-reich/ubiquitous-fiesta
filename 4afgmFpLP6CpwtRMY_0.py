
def sudoku_validator(x):
  for i in x:
    if len(set(i))!=9: 
      return False
  for i in range(9):
    if len(set([x[a][i] for a in range(9)]))!=9: 
      return False
  for i in range(0,9,3):
    for j in range(0,9,3):
      temp=x[i][j:j+3]+x[i+1][j:j+3]+x[i+2][j:j+3]
      if len(set(temp))!=9:
        return False
  return True

