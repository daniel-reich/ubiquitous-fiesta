
def gcd(a, b):
  if a == 0: return b
  return gcd(b % a, a)
​
def lcm(n1, n2):
  return (n1 * n2)/gcd(n1, n2)

