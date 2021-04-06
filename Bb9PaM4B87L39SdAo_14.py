
def intersection_union(lst1, lst2):
  return [sorted(set(lst1) & set(lst2)), sorted(set(lst1) | set(lst2))]

