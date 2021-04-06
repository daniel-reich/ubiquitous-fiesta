
def is_anti_list(lst1, lst2):
  a = set(lst1) == set(lst2)
  b = all(i != j for i, j in zip(lst1, lst2))
  
  return a and b

