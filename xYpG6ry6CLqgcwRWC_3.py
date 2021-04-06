
def sum_two_smallest_nums(lst):
  lst = sorted(x for x in lst if x >= 0)
  return sum(lst[:2])

