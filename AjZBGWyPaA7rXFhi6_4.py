
def min_swaps(s1, s2):
  count = 0
  for i, v in enumerate(s1):
    if s1[i] != s2[i]:
      count += 1
  return count/2

