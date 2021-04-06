
def gcd(a, b):
  if a < b: a, b = b, a
  while b > 0:
    a, b = b, a % b
  return a
  
def lcm(a, b):
  g = gcd(a, b)
  return a * b // g
​
def lcm_three(num):
  a, b, c = num
  return lcm(lcm(a,b), lcm(b,c))

