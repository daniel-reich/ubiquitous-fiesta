
def return_unique(lst):
  l = []
  for x in lst:
    if lst.count(x) == 1:
      l.append(x)
  return l

