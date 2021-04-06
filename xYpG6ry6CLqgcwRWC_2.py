
def sum_two_smallest_nums(lst):
  lst = sorted([item for item in lst if item >= 0])
  return lst[0]+lst[1]

