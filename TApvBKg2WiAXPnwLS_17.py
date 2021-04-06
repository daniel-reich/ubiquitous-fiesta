
def nth_smallest(lst, n):
  lst.sort()
  try:
    return lst[n-1]
  except IndexError:
    return None

