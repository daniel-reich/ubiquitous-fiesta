
def simple_comp(lst1, lst2):
  if not lst1 and not lst2:
    return lst1 == [] == lst2
    
  for i in lst1:
    if i*i not in lst2:
      return False
    lst2.pop(lst2.index(i*i))
  return lst1 != []

