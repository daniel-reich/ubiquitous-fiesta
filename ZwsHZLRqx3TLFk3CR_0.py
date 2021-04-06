
def eval_factorial(lst):
  return sum(fac(int(k[:-1])) for k in lst)
​
def fac(n):
  return n*fac(n-1) if n else 1

