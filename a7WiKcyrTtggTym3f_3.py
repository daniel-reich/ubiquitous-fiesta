
def gcd(a,b):
  if b==0:
    return a
  return gcd(b, a%b)
  
def lcm(a, b):
  return gcd(a,b)*(a//gcd(a,b))*(b//gcd(a,b))

