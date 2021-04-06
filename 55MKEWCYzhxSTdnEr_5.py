
def gcd(a, b):
  big = max(a,b)
  small = min(a,b)
  ans = big%small
  if ans == 0:
    return small
  while ans != 0:
    big = small
    small = ans
    ans = big%small
  return small

