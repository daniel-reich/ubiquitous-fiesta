
def simplify_sqrt(n):
  m = n
  k = 1
  for i in range(2,n+1):
    while n%(i**2) == 0:
      k *= i
      n /= i**2
  return (k,m/(k**2))

