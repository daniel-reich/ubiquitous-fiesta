
def how_many_missing(lst):
  c = 0
  if lst:
    for i in range(lst[0],lst[-1]+1):
      if i not in lst:
        c += 1
  return c

