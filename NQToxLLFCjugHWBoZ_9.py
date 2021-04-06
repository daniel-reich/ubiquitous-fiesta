
def sort_by_character(lst, n):
  lst.sort(key=lambda v: (isinstance(v, str), v[n-1]))
  return lst

