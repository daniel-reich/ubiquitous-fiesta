
def min_swaps(s1, s2):
  n = 0
  for i in range(len(s1)):
    if(s1[i] != s2[i]):
      n += 1
  return n//2

