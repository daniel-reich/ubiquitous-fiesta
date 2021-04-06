
def intersection_union(lst1, lst2):
  return [sorted(list(set(lst1).intersection(set(lst2)))), sorted(list(set(lst1).union(set(lst2))))]

