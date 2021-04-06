
def count_missing_nums(lst):
  out = [int(i) for i in lst if i.isdigit()]
  return sum(i not in out for i in range(min(out), max(out)+1))

