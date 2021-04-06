
def overlap(s1, s2):
  for i in range(len(s1)-1):
    substring = s1[i:len(s1)]
    if substring in s2:
      return s1[:i] + s2
  return s1 + s2

