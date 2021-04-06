
def nth_smallest(lst, n):
  if len(lst) < n: return None
  return sorted(lst)[n-1]

