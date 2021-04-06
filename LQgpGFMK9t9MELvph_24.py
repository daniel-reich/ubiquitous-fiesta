
def get_diagonals(l):
  if not l: 
    return [[], []]
  lenn = len(l[0])
  return [[l[i][i] for i in range(lenn)], [l[i][lenn-1-i] for i in range(lenn)]]

