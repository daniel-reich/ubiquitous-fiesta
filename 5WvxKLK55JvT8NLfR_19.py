
def diag_dom(lst):
  for i in range(0, len(lst)):
    summ = 0
    for j in lst[i]:
      summ += abs(j)
    if abs(lst[i][i]) <= summ - abs(lst[i][i]):
      return False
  return True

