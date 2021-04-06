
def gcd(a, b):
  a, b = max(a, b), min(a, b)
  return a if b == 0 else gcd(b, a % b)
​
def lcm(a, b):
  c = gcd(a, b)
  return a * b / c

