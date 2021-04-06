
def sexy_primes(n, limit):
  a=[i for i in range(1,limit) if prim(i)]
  if n==2:
    b=[(a[i],a[i]+6) for i in range(len(a)) if a[i]+6 in a]
  if n==3:
    b=[(a[i],a[i]+6, a[i]+12) for i in range(len(a)) if a[i]+6 in a and a[i]+12 in a]
​
  return b
​
def prim(i):
  if i==1:
    return False
  for j in range(2, i):
    if i%j==0:
      return False
  else:
    return True

