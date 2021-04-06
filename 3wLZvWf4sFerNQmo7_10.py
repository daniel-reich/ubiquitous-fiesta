
def neutralise(s1, s2):
  return ''.join([s1[i] if s1[i] == s2[i] else '0' for i in range(len(s1))])

