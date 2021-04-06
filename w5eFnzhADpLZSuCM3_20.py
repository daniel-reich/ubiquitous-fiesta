
def multiplicity(lst):
  l = []
  for x in lst:
    if all(x != y[0] for y in l):
      l.append([x, lst.count(x)])
  return l

