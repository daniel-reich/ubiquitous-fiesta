
def overlap(s1, s2):
  l=""
  z=""
  s=0
  v=0
  if len(s1)<len(s2):
    v=len(s1)
  else:
    v=len(s2)
  for i in range(v):
    p=s1[len(s1)-1-i:]
    if s2[:i+1]==p and len(p)>1:
      return s1+s2[len(p):]
  return s1+s2

