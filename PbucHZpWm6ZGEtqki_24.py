
def sliding_sum(lst, n, k):
  ans = []
  for i in range(len(lst)-n+1):
    if sum(lst[i:i+n])==k: 
      ans = ans + [lst[i:i+n]]
  return ans

