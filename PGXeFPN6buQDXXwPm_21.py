
def trace(lst):
  total = 0
  for x in range(0,len(lst)):
    total += lst[x][x]
  return total

