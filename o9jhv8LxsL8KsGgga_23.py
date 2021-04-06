
def bound_sort(lst, bounds):
  sortedBound = sorted(lst[bounds[0]:bounds[1] + 1])
  sortedLst = sorted(lst)
  return (sortedBound + lst[bounds[1] + 1:]) == sortedLst

