
def prod(x):
  r=1
  for i in str(x): r*=int(i)
  return r
​
def max_product(n):
  m,r = 0,[]
  for i in range(n+1):
    x=prod(i)
    if x>m: m,r = x,[i]
    elif x==m: r.append(i)
  return r

