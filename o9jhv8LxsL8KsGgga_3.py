
def bound_sort(lst, bounds):
  a, b = bounds
  return sorted(lst[:b + 1]) + lst[b + 1:] == sorted(lst)

