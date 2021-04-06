
def bound_sort(lst, bounds):
  lst2 = sorted(lst[bounds[0]:bounds[1]+1]) + lst[bounds[1]+1:]
  return lst2 == sorted(lst)

