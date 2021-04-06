
def nth_smallest(lst, n):
  return None if n > len(lst) else sorted(lst).pop(n-1)

