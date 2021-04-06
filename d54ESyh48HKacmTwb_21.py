
def find_gcd(x, y):
  while(y):
    x, y = y, x % y
  return x
​
def gcd(lst):
  g = find_gcd(lst[0], lst[1])
  for i in range(2, len(lst)):
    g = find_gcd(g, lst[i])
  return g

