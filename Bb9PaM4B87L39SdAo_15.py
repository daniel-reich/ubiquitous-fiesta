
def intersection_union(lst1, lst2):
  a,b = set(lst1),set(lst2)
  return [sorted(list(a&b)),sorted(list(a|b))]

