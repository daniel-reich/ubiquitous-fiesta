
def combinations(k, n):
  return fact(n)/(fact(n-k)*fact(k))
  
def fact(n):
  return not n or n * fact(n-1)

