
def diag_dom(lst):
  lst = [[abs(x) for x in y] for y in lst]
  return all(lst[i][i] > sum(lst[i]) / 2 for i in range(len(lst)))

