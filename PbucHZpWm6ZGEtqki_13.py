
def sliding_sum(lst, n, k):
  return [lst[i:i+n] for i in range(len(lst)-n+1) if sum(lst[i:i+n])==k]

