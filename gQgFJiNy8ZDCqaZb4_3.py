
def overlap(s1, s2):
  trim = []
  if s1 == s2:
    return s1
  for i in range(len(s2)):
    trim.append(s2[i])
    if ''.join(trim) not in s1 or i == len(s2) - 1:
      if ''.join(trim[:-1]) != s1[-(len(trim) - 1):]:
        return s1+s2
      return s1 + s2[i:]

