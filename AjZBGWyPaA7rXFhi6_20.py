
def min_swaps(s1, s2):
  return len([x for x, y in zip(s1,s2) if x != y])/2

