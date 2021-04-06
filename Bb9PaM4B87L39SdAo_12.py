
def intersection_union(lst1, lst2):
  set1 = set(lst1)
  set2 = set(lst2)
  intersection = list(set1.intersection(set2))
  union = list(set1.union(set2))
  union.sort()
  intersection.sort()
  lst = [intersection, union]
  return lst

