
def diag_dom(lst):
  return all(sum(map(abs, lst[r]))-abs(lst[r][r]) < abs(lst[r][r]) for r in range(len(lst)))

