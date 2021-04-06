
def sim_prop_frac(max_den):
  return sum(gcd(n,d)==1 for n in range(1,max_den+1) for d in range(1,max_den+1) if n<d)
  
​
def gcd(a,b):
  while a:
    a,b = b%a,a
  return b

