
def i_sqrt(n):
  from math import sqrt
  m=0
  if n<0:
      return 'invalid'
  while n>=2:
      n=sqrt(n)
      m+=1
  return m

