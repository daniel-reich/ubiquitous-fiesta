
def min_swaps(s1, s2):
  c = s2.count('1')
  a = 0
  for i in range(len(s1)):
    if s1[i] != s2[i]:
      a += 1
  return a // 2

