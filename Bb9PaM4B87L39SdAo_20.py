
def intersection_union(lst1, lst2):
  return [sorted(set([x for x in lst1 if x in lst2])), sorted(set(lst1 + lst2))]

