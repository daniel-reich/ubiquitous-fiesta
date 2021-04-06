
def nth_smallest(lst, n):
  lst.sort()
  if n > len(lst):
    return None
  else:
    return lst[n - 1]

