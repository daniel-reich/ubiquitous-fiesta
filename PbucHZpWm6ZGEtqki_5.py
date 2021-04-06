
def sliding_sum(lst, n, k):
  l=[lst[i:i+n] for i in range(len(lst)-(n-1))]
  return [c for c in l if sum(c)==k]

