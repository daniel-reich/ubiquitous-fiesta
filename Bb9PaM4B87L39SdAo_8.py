
def intersection_union(lst1, lst2):
  i = list(set(lst1).intersection(set(lst2)))
  s = list(set(lst1).union(set(lst2)))
  return [sorted(i), sorted(s)]

