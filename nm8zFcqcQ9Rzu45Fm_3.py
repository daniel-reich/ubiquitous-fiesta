
def bridge_shuffle(lst1, lst2):
  for i, n in enumerate(lst2):
    lst1.insert(i+i+1, n)
  return lst1

