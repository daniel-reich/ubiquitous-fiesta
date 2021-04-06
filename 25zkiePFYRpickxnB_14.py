
def count_boomerangs(lst):
  numberOfBooms = 0
  for i in range (len(lst)-2):
    if lst[i] == lst[i+2] and lst[i] != lst[i+1]:
      numberOfBooms += 1
  return numberOfBooms

