
def nth_smallest(lst, n):
  a=sorted(lst)
  b=len(a)
  if b<n:
    return None
  else:
    return a[n-1]

