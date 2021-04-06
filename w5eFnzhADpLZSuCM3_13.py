
def multiplicity(lst):
  lst2 = []
  lst3 = []
  for i in lst:
    if i in lst2:
      continue
    else:
      lst2.append(i)
      lst3.append([i, lst.count(i)])
  return lst3

