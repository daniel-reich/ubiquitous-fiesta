
def how_many_missing(lst):
  return lst[-1] - lst[0] - len(lst) + 1 if lst else 0

