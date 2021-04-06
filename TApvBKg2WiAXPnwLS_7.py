
def nth_smallest(lst, n):
  lst.sort()
  
  if len(lst) < n:
    return None
  
  return lst[n - 1]

