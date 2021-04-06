
def multiplicity(lst):
  a = []
  for i in lst:
    if i not in a:
      a.append(i)
  return [[i,lst.count(i)] for i in a]

