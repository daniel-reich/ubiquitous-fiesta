
def overlap(s1, s2):
  index = len(s1)
  for i in range(len(s1)):
    if s2.startswith(s1[i:]):
      index = i
      break
  return s1[:index] + s2

