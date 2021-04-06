
def simple_comp(lst1, lst2):
  if lst1==None or lst2==None:
    return lst1==lst2
  return sorted(x**2 for x in lst1)==sorted(lst2)

