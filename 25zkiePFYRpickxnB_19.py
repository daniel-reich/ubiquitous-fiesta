
def count_boomerangs(lst):
  return sum(a == c != b for a, b, c in zip(lst, lst[1:], lst[2:]))

