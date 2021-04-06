
def min_swaps(s1, s2):
  diff = 0
  for i in range(len(s1)):
    if s1[i] != s2[i]:
      diff += 1
  return diff//2

