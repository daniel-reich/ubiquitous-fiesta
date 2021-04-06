
def moving_partition(lst):
  if not lst:
    return []
  return [[lst[0 : i + 1], lst[i + 1:]] for i in range(len(lst) - 1)]

