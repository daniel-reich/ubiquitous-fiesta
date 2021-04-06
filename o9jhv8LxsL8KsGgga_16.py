
def bound_sort(lst, bounds):
  return sorted(lst[bounds[0]:bounds[1]+1])+lst[bounds[1]+1:]==sorted(lst)

