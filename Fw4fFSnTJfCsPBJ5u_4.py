
def how_many_missing(lst):
  return 0 if not lst else len(range(lst[0],lst[-1]+1)) - len(lst)

