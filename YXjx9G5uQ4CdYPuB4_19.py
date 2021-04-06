
def simple_comp(lst1, lst2):
  try:
    lst1 = sorted([i**2 for i in lst1])
    lst2.sort()
  except:
    return False
    
  return lst1 == lst2

