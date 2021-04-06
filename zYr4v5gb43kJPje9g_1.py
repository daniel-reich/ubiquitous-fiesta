
def moving_partition(lst):
  ll= len(lst)
  if ll==0: return []
  elif ll==1: return ['???']
  
  return [[lst[:i], lst[i:]] for i in range(1,ll)]

