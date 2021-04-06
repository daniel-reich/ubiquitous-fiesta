
def is_anti_list(lst1, lst2):
  if lst1 == lst2: return True 
  for x in lst1:
    if x not in set(lst2): return False 
  return True

