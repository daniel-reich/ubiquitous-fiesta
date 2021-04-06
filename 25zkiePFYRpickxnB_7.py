
def count_boomerangs(lst):
  return sum([1 for i in range(len(lst)-1) if lst[i:i+3][0] == lst[i:i+3][-1] and lst[i:i+3][0] != lst[i:i+3][1]])

