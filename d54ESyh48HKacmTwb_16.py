
def gcd2(a, b):
    while b != 0:
       t = b
       b = a % b
       a = t
    return a
​
def gcd(lst):
  g = gcd2(lst[0], lst[1])
  for k in lst[2:]:
    g = gcd2(g, k)
  return g

