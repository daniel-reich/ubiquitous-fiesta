
def bound_sort(lst, bounds):
  if not lst[bounds[1] + 1:]:
    return True
  return sorted(lst[bounds[1] + 1:]) == lst[bounds[1] + 1:] and (max(lst[0:bounds[1] + 1]) < min(lst[bounds[1] + 1:]))

