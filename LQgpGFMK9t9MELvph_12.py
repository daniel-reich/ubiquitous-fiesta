
def get_diagonals(lst):
  diag1 = []
  diag2 = []
  n = len(lst)
  i = 0
  while i < n:
    print(i, lst[i][i])
    diag1.append(lst[i][i])
    print(":",i, lst[i][n-i-1])
    diag2.append(lst[i][n-i-1])
    i = i+1
  return ([diag1, diag2])

