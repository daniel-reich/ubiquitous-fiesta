
def nth_smallest(lst, n):
  try:
    lst.sort()
    return lst[n-1]
  except IndexError:
    return None

