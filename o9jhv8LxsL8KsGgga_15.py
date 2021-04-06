
def bound_sort(lst, bounds):
  start, end = bounds[0], bounds[1]
  return sorted(lst[start:end+1]) + lst[end+1:] == sorted(lst)

