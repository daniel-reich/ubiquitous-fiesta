
def overlap(s1, s2):
  n1,n2=len(s1),len(s2)
  n = min(n1,n2)
  for i in range(n+1):
    if s1[-n+i:] == s2[:n-i]:
      return s1+s2[n-i:]
  return s1+s2

