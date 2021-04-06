
def how_many_missing(lst):
  if lst == []: return 0
  return sum([1 for x in range(lst[0], lst[-1]) if x not in lst])

