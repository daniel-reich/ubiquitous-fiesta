
def count_boomerangs(lst):
  boomerangs = 0
  i = 1
  while i < len(lst) - 1:
    if(lst[i-1] < lst[i] and lst[i+1] < lst[i] and lst[i-1] == lst[i+1]):
      boomerangs += 1
    if(lst[i-1] > lst[i] and lst[i+1] > lst[i] and lst[i-1] == lst[i+1]):
      boomerangs += 1
    i += 1
  return boomerangs

