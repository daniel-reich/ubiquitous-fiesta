
def how_many_missing(lst):
  if lst:
    return len(list(range(lst[0], lst[-1] + 1))) - len(lst)
  return 0

