
def simple_comp(lst1, lst2):
  x = False
  if (type(lst1) == list and type(lst2) == list):
    x = (sorted([x**2 for x in lst1]) == sorted(lst2))
  return x

