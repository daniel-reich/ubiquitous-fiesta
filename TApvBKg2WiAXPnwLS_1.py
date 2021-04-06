
def nth_smallest(lst, n):
  return sorted(lst)[n-1] if len(lst) >= n else None

