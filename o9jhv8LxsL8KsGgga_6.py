
def bound_sort(lst, b):
  x = b[1]+1
  return sorted(lst[:x]) + lst[x:] == sorted(lst)

