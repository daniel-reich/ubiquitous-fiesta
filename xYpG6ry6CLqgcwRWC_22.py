
def sum_two_smallest_nums(lst):
  lst = sorted(filter(lambda x:x>=0, lst))
  return lst[0] + lst[1]

