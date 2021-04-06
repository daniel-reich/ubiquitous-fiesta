
def bound_sort(lst, bounds):
  lo, hi = bounds
  return sorted(lst) == lst[:lo] + sorted(lst[lo:hi+1]) + lst[hi+1:]

