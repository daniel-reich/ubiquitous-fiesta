
def get_diagonals(lst):
  diag1 = [lst[i][i] for i in range(len(lst))]
  diag2 = [lst[i][len(lst)-1-i] for i in range(len(lst))]
  return [diag1, diag2]

