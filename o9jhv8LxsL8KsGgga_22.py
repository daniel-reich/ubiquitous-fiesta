
def bound_sort(lst, bounds):
  lst_2 = [x for x in lst]
  lst_2.sort()
  bound = lst[bounds[0]: bounds[1]+1]
  rest = lst[bounds[1]+1: ]
  bound.sort()
  return lst_2 == (bound +rest)

