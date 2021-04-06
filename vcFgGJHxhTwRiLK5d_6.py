
def smallest(n):
  def gcd(a,b):
    while a>0:
      a,b = b%a,a
    return b
  
  def lcm(a,b): return a*b//gcd(a,b)
  
  s=1
  for i in range(1,n+1):
    s = lcm(s,i)
  return s

