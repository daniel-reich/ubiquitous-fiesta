
def sort_by_character(lst, n):
  x = lst
  x.sort(key = lambda x: x[n - 1])
  return x

