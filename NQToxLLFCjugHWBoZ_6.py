
def sort_by_character(lst, n):
  lst.sort(key = lambda x: x[n-1])
  return lst

