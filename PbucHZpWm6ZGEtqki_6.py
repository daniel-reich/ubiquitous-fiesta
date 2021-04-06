
def sliding_sum(lst, n, k):
  lst = [lst[i:i+n] for i in range(len(lst)-n+1)]
  return list(filter(lambda x:sum(x) == k,lst))

