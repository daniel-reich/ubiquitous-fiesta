
def n_differences(lst):
  if len(lst) == 1:
    return lst[0]
  return n_differences([y-x for x, y in zip(lst[:-1], lst[1:])])

