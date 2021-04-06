
def intersection_union(lst1, lst2):
  return [sorted([v for v in set(lst1) if v in set(lst2)]), 
  sorted(list(set(lst1 + lst2)))]

