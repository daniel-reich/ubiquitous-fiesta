
def sum_two_smallest_nums(lst):
  return sum([e for e in sorted(lst) if e > 0][:2])

