
def count_boomerangs(lst):
  count = 0
  if(len(lst) < 2): return count
  for x in range(len(lst)):
    if x >= len(lst) - 2: return count
    elif lst[x] == lst[x+2] and lst[x] != lst[x+1]:
      count += 1
  return count

