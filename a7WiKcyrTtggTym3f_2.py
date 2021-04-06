
def lcm(a, b):
  def gcd(a,b):
    return a if not b else gcd(b,a%b)
  return (a*b)/gcd(a,b)

