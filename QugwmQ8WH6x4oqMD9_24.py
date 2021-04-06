
def count_identical_lists(*lsts):
  return sum(lsts.count(lst) > 1 for lst in lsts)

