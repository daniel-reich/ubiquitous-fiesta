
def get_diagonals(lst):
  x = []
  y = []
  for i in range(len(lst)):
    x.append(lst[i][i])
    y.append(lst[i][-1 - i])
  return [x, y]

