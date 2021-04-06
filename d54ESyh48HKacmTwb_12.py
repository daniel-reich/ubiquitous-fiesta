
def gcd(lst):
  lst = sorted(lst)
  g = func(lst[0],lst[1])
  for i in range(2,len(lst)):
    g = func(g,lst[i])
  return g
  
def func(a,b):
  if b%a==0:
    return a
  return func(b,a%b)

