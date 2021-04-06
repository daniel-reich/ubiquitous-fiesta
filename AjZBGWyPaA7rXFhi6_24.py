
def min_swaps(s1, s2):
  dif = 0
  for i in range(len(s1)):
    if s1[i] != s2[i]:
      dif += 1
  return dif//2

