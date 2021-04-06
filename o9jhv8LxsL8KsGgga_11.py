
def bound_sort(lst, bounds):
  sorted_list = lst[:bounds[0]] + sorted(lst[bounds[0]:bounds[1] + 1]) + lst[bounds[1] + 1:]
  return sorted_list == sorted(lst)

