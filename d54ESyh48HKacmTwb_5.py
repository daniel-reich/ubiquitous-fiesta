
def gcd(lst):
  d = lst[0]
  for n in lst[1:]:
    d = gcd2(d,n)
  return d
​
def gcd2(a,b):
  while a:
    a,b = b%a,a
  return b

