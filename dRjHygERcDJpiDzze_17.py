
def lengthen(s1, s2):
  if len(s1) < len(s2):
    s1, s2 = s2, s1
  return s2*(len(s1)//len(s2))+s2[:len(s1)%len(s2)]

