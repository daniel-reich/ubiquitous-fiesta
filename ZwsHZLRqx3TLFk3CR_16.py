
def fac(n):
  if n==0 or n==1:
    return 1
  return n*fac(n-1) 
def eval_factorial(lst):
  return sum([fac(int(l[:-1])) for l in lst])

