
def min_length(lst, n):
  s = sum(lst)
  if lst:
    x = min_length(lst[1:], n)
    y = min_length(lst[:-1], n)
    return min((k for k in (x, y) if k >= 0), default = len(lst) if s > n else -1)
  return -1

