
def intersection_union(lst1, lst2):
  lst3 = sorted(list(set(lst1) & set(lst2)))
  lst4 = sorted(list(set(lst1) | set(lst2)))
  return [lst3,lst4]

