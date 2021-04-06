
def diag_dom(lst):
  for i in range(len(lst)):
    row_sum = 0
    for j in range(len(lst)):
      row_sum += abs(lst[i][j])
    if row_sum>=2*abs(lst[i][i]):
      return False
  return True

