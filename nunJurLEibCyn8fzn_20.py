
def filter_list(lst):
  new_l = []
  for x in lst:
    if isinstance(x, int):
      new_l.append(x)
  return new_l

