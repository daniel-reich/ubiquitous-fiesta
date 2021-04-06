
def min_swaps(s1, s2):
  return sum(1 if s1[i]!=s2[i] else 0 for i in range(len(s1)))/2

