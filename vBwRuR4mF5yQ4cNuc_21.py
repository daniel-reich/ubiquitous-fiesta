
def count_missing_nums(lst):
  l = [int(x) for x in lst if x.isnumeric()]
  return sum(i not in l for i in range(min(l),max(l)))

