
def replace_next_largest(lst):
  l = lst[:]
  l.sort()
  res = []
  for el in lst:
    i = l.index(el)
    if el == l[-1]:
      res.append(-1)
    else:
      res.append(l[i+1])
  return res

