
def min_swaps(s1, s2):
  return sum([x[0] != x[1] for x in zip(s1,s2)])/2

