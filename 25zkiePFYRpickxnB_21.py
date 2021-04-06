
def count_boomerangs(lst):
  return sum([1 for n in range(len(lst)-2) if lst[n] == lst[n+2] and lst[n] != lst[n+1]])

