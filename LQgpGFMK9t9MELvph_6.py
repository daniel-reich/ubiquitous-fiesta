
def get_diagonals(lst):
  n = len(lst)
  main_diag = [lst[i][i] for i in range(n)]
  off_diag = [lst[i][n-1-i] for i in range(n)]
  return [main_diag, off_diag]

