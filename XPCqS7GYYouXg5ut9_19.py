
def simplify_sqrt(n):
  a = 1
  b = 1
  for x in range(1,100001):
    if n % (x**2) == 0:
      a = x
  b = n / a**2
  return (a,b)

