
def make_sandwich(i, f):
  l = []
  for j in i: l += [[j], ['bread',j,'bread']][j == f]
  return l

