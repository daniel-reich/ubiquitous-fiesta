
def moving_partition(lst):
  result = []
  for i in range(1,len(lst)):
    result.append([lst[:i], lst[i:]])
  return result

