
def count_identical_lists(lst1, lst2, lst3, lst4):
  lsts = [lst1,lst2,lst3,lst4]
  if len(set(tuple(i) for i in lsts)) == 4:
    return 0
  return 5 - len(set(tuple(i) for i in lsts))

