
def sim_prop_frac(max_den):
  lst = []
  for d in range(max_den+1):
    for n in range(1,d):
      if gcd(d,n)==1 or str(n//gcd(d,n))+'/'+str(d//gcd(d,n)) not in lst:
        lst.append(str(n)+'/'+str(d))
  return len(lst)
​
def gcd(a,b): 
    if(b==0): 
        return a 
    else: 
        return gcd(b,a%b)

