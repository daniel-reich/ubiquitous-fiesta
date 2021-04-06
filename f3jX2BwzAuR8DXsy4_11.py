
def fac(n):
  return 1 if n<2 else n*fac(n-1)
def fact_of_fact(n):
  p=1
  for i in range(1, n+1):
    p*=fac(i)
  return p

