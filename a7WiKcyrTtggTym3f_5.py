
def lcm(a, b):
​
  def gcd(a,b): 
    if a == 0: 
      return b 
    return gcd(b % a, a) 
  
  return (a*b) / gcd(a,b)

