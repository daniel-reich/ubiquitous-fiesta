
def fact(n):
  return n < 2 or n * fact(n-1)
​
def combinations(k, n):
  result = fact(n)/(fact(n-k)*fact(k))
  return result

