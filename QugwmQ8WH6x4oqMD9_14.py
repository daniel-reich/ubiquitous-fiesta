
def count_identical_lists(lst1, lst2, lst3, lst4):
  l = [lst1, lst2, lst3, lst4]
  c = max([l.count(lst) for lst in l])
  if c == 1:
    return 0
  return c

