
def gcd(n1, n2):
  n = min(n1,n2)
  while n>0:
    if not n1%n and not n2%n:
      return n
    n-=1

