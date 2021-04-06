
def lengthen(s1, s2):
  l1=len(s1)
  l2=len(s2)
  if(l1>l2):
    a=s2*10
    r=l1-l2
    return s2+a[:r]
  else:
    a=s1*10
    r=l2-l1
    return s1+a[:r]

