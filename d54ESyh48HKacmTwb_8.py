
def gcd_n(a, b):
  return a if b==0 else gcd_n(b, a%b)
def gcd(lst):
  return gcd_n(lst[0], lst[1]) if len(lst)==2 else gcd_n(lst[0], gcd(lst[1:]))

