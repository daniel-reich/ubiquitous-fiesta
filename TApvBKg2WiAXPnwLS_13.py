
def nth_smallest(lst, n):
  ordered = sorted(lst)
  if n > len(lst):
    return None
  else:
    return ordered[n - 1]

