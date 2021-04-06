
def intersection_union(lst1, lst2):
  return [intersection(lst1,lst2),union(lst1,lst2)]
  
def intersection(a,b):
  return sorted(list(set(a)&set(b)))
  
def union(a,b):
  return sorted(list(set(a+b)))

