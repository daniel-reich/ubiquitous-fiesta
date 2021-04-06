
def unique_lst(lst):
  return [x for i, x in enumerate(lst) if x > 0 and x not in lst[:i]]

