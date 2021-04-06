
def count_identical_lists(*lst):
  lst = [tuple(i) for i in lst]
  return sum(lst.count(i) for i in set(lst) if lst.count(i) > 1)

