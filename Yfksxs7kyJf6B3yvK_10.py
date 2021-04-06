
def min_miss_pos(lst):
  l = sorted(set(lst))
  return min(x for x in list(range(1, l[-1]+2)) if x not in l)

