
def sum_two_smallest_nums(lst):
  a = sorted(list(filter(lambda x: x > 0, lst)))
  return a[0] + a[1]

