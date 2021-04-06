
def multiplicity(lst):
  c = lst[::-1]
  for i in lst:
    while c.count(i) > 1:
      c.remove(i)
  return [[i,lst.count(i)] for i in c[::-1]]

