
def intersection_union(lst1, lst2):
  return [sorted(list(set([l1 for l1 in lst1 for l2 in lst2 if l1==l2]))),sorted(list(set(lst1+lst2)))]

