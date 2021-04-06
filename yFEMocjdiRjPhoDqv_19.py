
def f(m):
  s=0
  if m<2: return False
  else:
    for i in range(1,m+1):
      if m%i==0: s+=1
    return s==2
def prime_in_range(n1, n2):
  return any(map(f,range(n1,n2+1)))

