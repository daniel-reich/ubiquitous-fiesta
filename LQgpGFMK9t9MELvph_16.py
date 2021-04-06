
def get_diagonals(lst):
  diag1 = [lst[i][i] for i in range(len(lst))]
  diag2 = [lst[i][-i-1] for i in range(len(lst))]
  return [diag1, diag2]

