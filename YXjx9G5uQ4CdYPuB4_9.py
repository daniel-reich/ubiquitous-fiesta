
def simple_comp(lst1, lst2):
  if lst1 == None or lst2 == None:
    return False
  return sorted(lst2) == sorted([i * i for i in lst1])

