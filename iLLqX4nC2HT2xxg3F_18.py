
def deepest(lst):
  mx = 0
  for x in lst:
    if type(x) is list:
      mx=max(mx, deepest(x))
  return mx+1

