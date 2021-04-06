
def moving_partition(lst):
  ret = []
  for i in range(1, len(lst)):
    ret.append([lst[:i], lst[i:]])
  return ret

