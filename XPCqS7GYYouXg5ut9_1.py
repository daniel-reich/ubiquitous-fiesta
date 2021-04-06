
def simplify_sqrt(n):
  hi_sqr = next(i for i in range(n,0,-1) if not n%i and not i**0.5%1)
  return (hi_sqr**0.5, n/hi_sqr)

