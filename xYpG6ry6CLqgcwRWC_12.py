
def sum_two_smallest_nums(lst):
  lst = sorted([i for i in lst if i >= 0])
  return lst[0] + lst[1]

