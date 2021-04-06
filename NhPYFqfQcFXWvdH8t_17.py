
# ax+by=gcd(x,y)
# gives vector [gcd,a,b]
def ext_euc_alg(x, y):
  if x==0:
    return [y, 0, 1]
  else:
    [gcd, ao, bo]=ext_euc_alg(y%x, x)
    a=bo-(y//x)*ao
    b=ao
    return [gcd, a, b]
​
def mod_inv(n, m):
  [gcd, a, b]=ext_euc_alg(n,m)
  if gcd!=1:
    return False
  else:
    if a<0:
      return a+m
    else:
      return a

