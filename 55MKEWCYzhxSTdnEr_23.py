
def gcd(a, b):
  return max(x for x in range(1, a+b) if not (a % x or b % x))

