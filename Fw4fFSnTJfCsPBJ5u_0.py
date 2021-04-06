
def how_many_missing(lst):
  return len(lst) and lst[-1] - lst[0] - len(lst) + 1

