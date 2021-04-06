
def min_swaps(s1, s2):
  return len([x for x in range(len(s1)) if s1[x]!=s2[x]])/2

