
def is_prim_pyth_triple(lst):
  c = max(lst)
  lst.remove(c)
  a,b = lst
  def gcd(a,b):
    return a if not b else gcd(b, a%b)
  return a**2 + b**2 == c**2 and gcd(a,b) == 1 and gcd(b,c) == 1 and gcd(a,c)==1

