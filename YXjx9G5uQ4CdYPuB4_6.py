
def simple_comp(lst1, lst2):
  if type(lst1)!=list or type(lst2)!=list: return False
  return sorted([i*i for i in lst1]) == sorted(lst2)

