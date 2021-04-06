
def gcd(x, y):
  if y==0:
    return x
  else:
    return gcd(y,x%y)
​
def is_prim_pyth_triple(lst):
  [a, b, c]=sorted(lst)
  if a**2 + b**2 == c**2:
    if gcd(a, b)==1 and gcd(b, c)==1 and gcd(a, c)==1:
      return True
    else:
      return False
  else:
    return False

