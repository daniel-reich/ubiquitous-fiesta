
def intersection_union(lst1, lst2):
  s1, s2 = set(lst1), set(lst2)
  return [sorted(s1 & s2), sorted(s1.union(s2))]

