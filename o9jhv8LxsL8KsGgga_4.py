
def bound_sort(lst, bounds):
  l=lst[:bounds[0]]+sorted(lst[bounds[0]:bounds[-1]+1])+lst[bounds[-1]+1:]
  return l ==sorted(lst)

