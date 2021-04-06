
def lengthen(s1, s2):
  if len(s1) > len(s2):
    while len(s1) > len(s2):
      s2 += s2
    return s2[:len(s1)]
  else:
    while len(s1) < len(s2):
      s1 += s1
    return s1[:len(s2)]

