
def repetition(t,n):
  n-=1
  if n==0:
    return t
  return repetition(t,n)+t

