
def bound_sort(lst, bounds):
  i = bounds[1] + 1
  return sorted(lst) == sorted(lst[:i]) + lst[i:]

