
def gcd(a, b):
  for i in range(max(a,b),0,-1):
    if a % i == 0 and b % i == 0:
      return i

