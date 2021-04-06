
def intersection_union(lst1, lst2):
  inter = sorted(list(set(lst1).intersection(set(lst2))))
  un = sorted(list(set(lst1).union(set(lst2))))
  return[inter, un]

