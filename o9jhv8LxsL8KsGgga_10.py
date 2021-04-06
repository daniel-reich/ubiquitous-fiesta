
def bound_sort(lst, bounds):
  lst[0:bounds[1]+1] = sorted(lst[0:bounds[1]+1])
  return sorted(lst) == lst

