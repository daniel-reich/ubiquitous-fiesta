
def bound_sort(lst, bounds):
  limit = bounds[1] + 1
  return sorted(lst[:limit]) + lst[limit:] == sorted(lst)

