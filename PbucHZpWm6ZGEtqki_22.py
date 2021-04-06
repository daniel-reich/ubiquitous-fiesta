
def sliding_sum(lst, n, k):
  return [lst[i:i+n] for i in range(0, len(lst) - n + 1) if sum(lst[i:i+n]) == k]

