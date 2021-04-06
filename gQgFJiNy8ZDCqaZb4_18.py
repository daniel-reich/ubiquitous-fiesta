
def overlap(s1, s2):
  for x in range(len(s1)):
    if s2.startswith(s1[x:]):
      return s1[:x]+s2
  return s1+s2

