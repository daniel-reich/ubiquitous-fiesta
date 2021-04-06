
def min_swaps(s1, s2):
  return sum(0.5 for x, y in zip(s1, s2) if x != y)

