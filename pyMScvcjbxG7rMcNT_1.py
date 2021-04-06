
def sum_list(lst):
  if not lst: return 0
  if type(lst[0]) is int: return lst[0] + sum_list(lst[1:])
  return sum_list(lst[0]) + sum_list(lst[1:])

