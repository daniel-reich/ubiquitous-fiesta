
def simple_check(a, b):
  m=min(a,b)
  M=max(a,b)
  c=0
  while m:
    if M%m==0:
      c+=1
    M-=1
    m-=1
  return c

