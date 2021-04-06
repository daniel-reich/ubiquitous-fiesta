
def overlap(a,b):
  for i in range(len(b),0,-1):
    if a[a.rfind(b[:i]):]==b[:i]:return a+b[i:]
  return a+b

