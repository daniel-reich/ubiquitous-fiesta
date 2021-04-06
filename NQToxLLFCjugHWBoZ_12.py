
def sort_by_character(lst, n):
  lst.sort(key = lambda lst: lst[n-1])
  return lst

