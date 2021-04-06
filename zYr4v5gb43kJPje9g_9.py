
def moving_partition(lst):
  return [[lst[:i+1], lst[i+1:]] for i in range(len(lst)-1)]

