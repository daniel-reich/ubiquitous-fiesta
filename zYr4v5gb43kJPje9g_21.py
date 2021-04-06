
def moving_partition(lst):
  return [[lst[:i], lst[i:]] for i in range(1,len(lst))]

