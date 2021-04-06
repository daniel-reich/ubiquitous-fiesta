
def intersection_union(lst1, lst2):
  return [sorted(list(set(lst1) & set(lst2))), sorted(list(set(lst1 + lst2)))]

