
def get_diagonals(lst):
  a, b = [], []
  for i in range(len(lst)):
    a.append(lst[i][i])
    b.append(lst[i][-i-1])
  return [a, b]

