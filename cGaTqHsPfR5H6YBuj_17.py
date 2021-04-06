
def make_sandwich(ing, f):
  l = []
  for i in ing:
    if i == f:
      l += ['bread', i, 'bread']
    else:
      l += i
  return l

