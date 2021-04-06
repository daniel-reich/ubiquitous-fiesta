
def simple_comp(lst1, lst2):
  return sorted([x**2 for x in lst1])==sorted(lst2) if type(lst1)==type(lst2)==list else False

