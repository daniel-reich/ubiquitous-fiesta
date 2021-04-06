
def diag_dom(lst):
  for i in range(len(lst)):
    x = lst[i][:i] + lst[i][i+1:]
    if abs(lst[i][i]) <= sum([abs(e) for e in x]):
      return False
  return True

