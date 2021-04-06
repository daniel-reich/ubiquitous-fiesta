
def clear_ordering(lst):
  i1 = set([x[0] for x in lst])
  i2 = set([x[1] for x in lst])
  return len(i1) == len(lst) and len(i2) == len(lst)

