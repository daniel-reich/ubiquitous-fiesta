
def product_of_primes(num):
  a,n=0,2
  p=[x for x in range(num) if all(x%i for i in range(2,x))]
  while n<len(p):
    for m in range(n,len(p)):
      if p[n]*p[m]==num:
        a=a+1
    n=n+1
  return a!=0

