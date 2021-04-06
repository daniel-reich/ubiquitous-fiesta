
def count_boomerangs(lst):
  is_boomerang = lambda x: x[0] == x[-1] and len(set(x)) > 1
  return sum(is_boomerang(lst[i:i+3]) for i in range(len(lst)-2))

