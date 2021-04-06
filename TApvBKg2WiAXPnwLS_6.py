
def nth_smallest(lst, n):
  return sorted(lst)[n-1] if n <= len(lst) else None

