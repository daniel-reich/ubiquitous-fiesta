
def sum_two_smallest_nums(lst):
  return sum(sorted(filter(lambda x: x>0, lst))[:2])

