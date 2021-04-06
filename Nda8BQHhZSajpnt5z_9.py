
def gcd(a, b):
    while b != 0:
       t = b
       b = a % b
       a = t
    return a
​
def GCD(lst):
  g = gcd(lst[0], lst[1])
  for k in lst[2:]:
    g = gcd(k, g)
  return g

