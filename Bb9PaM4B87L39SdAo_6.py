
def intersection_union(l1, l2):
  l1 = sorted(list(set(l1)))
  l2 = sorted(list(set(l2)))
  
  union = sorted(list(set(l1+l2)))
  
  intersection = sorted([i for i in l1 if i in l2])
  
  return [intersection, union]

