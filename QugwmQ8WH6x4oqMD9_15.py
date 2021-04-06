
def count_identical_lists(*ls):
  return sum(ls.count(x) > 1 for x in ls)

