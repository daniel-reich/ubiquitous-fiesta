
def nth_smallest(lst, n):
  if n > len(lst): return None
  return sorted(lst)[n - 1]

