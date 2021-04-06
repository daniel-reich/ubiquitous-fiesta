
def lcm(a,b):
  def gcd(a,b):
    a,b = sorted((a,b))
    if b % a:
      return gcd(a, b%a)
    else:
      return a
  return (a*b)//gcd(a,b)

