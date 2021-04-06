
def how_many_missing(lst):
  return lst[-1] - lst[0] + 1 - len(lst) if lst else 0

