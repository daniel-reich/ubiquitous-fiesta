
def get_diagonals(lst):
  n = len(lst)
  d1 = [lst[i][i] for i in range(n)]
  d2 = [lst[i][n-i-1] for i in range(n)]
  return [d1, d2]

