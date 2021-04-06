
def sliding_sum(lst, n, k):
  res = []
  for i in range(0,len(lst)-n+1):
    if sum(lst[i:i+n])==k:
      res.append(lst[i:i+n])
  return res

