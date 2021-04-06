
def bound_sort(lst, bounds):
  l, h = bounds
  return sorted(lst[:h+1]) + lst[h+1:] == sorted(lst)

