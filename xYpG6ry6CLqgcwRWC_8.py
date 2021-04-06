
def sum_two_smallest_nums(lst):
  lst = filter(lambda x : x > 0, lst)
  return sum(sorted(lst)[0:2])

