
def sliding_sum(lst, n, k):
  return [lst[x:x+n] for x in range(len(lst) - n + 1) if sum(lst[x:x+n]) == k]

