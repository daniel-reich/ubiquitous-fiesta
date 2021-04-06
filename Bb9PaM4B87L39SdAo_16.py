
def intersection_union(lst1, lst2):
  return [sorted(list(set(lst1) & set(lst2))), list(set(lst1).union(set(lst2)))]

