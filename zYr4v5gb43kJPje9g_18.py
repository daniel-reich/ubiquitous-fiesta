
def moving_partition(lst):
  if len(lst)==0: return []
  res = []
  for i in range(len(lst)-1):
    res.append([lst[0:i+1],lst[i+1:]])
  return res

