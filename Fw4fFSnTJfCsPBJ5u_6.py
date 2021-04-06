
def how_many_missing(lst):
  count = 0
  if len(lst) == 0:
      return 0
  for x in range(lst[0], lst[-1]+1):
    if x not in lst:
      count+=1
  return count

