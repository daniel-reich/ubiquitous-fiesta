
def sudoku_validator(x):
  ch = {i for i in range(1,10)}
  if not all([set(i) == ch for i in x]): return False
  if not all([set(i) == ch for i in zip(*x)]): return False
  boxes = [[i[3*j:3*j+3] for i in x[3*i:3*i+3]] for i in range(3) for j in range(3)]
  for i in boxes:
    e=set()
    for j in i: e|=set(j)
    if e!=ch: return False
  return True

