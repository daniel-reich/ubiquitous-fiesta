
def sum_two_smallest_nums(lst):
  return sum(sorted([i for i in lst if i > 0])[0:2])

