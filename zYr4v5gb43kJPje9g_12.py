
def moving_partition(lst):
  if len(lst) <= 1:
    return lst
  return [[lst[:i], lst[i:]] for i in range(1, len(lst))]

