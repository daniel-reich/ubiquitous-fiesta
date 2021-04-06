
def block(lst):
  total = 0
  for x in range(len(lst[0])):
    for y in range(len(lst)-1, 0, -1):
      if lst[y][x] < lst[y-1][x]:
        total += len(lst) - y
  
  
  return total

