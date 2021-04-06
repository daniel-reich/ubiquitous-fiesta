
def lengthen(s1, s2):
  s,l=sorted([s1,s2],key=len)
  while len(s)<len(l):
    s+=s
  return s[:len(l)]

