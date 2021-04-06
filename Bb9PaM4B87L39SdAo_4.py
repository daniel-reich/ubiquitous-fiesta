
def intersection_union(lst1, lst2):
  union = sorted(set(lst1).union(set(lst2)))
  intersection = sorted(set(lst1).intersection(set(lst2)))
  return [intersection, union]

