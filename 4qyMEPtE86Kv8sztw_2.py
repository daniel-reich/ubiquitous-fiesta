
def binary_sum(lst):
  a,b = lst
  r = max(a[::-1].index("."),b[::-1].index("."))
  a,b = [x + "0"*(r-x[::-1].index(".")) for x in [a,b]]
  a,b = [x.replace(".","") for x in [a,b]]
  a,b = [sum(int(x[::-1][i])*2**i for i in range(len(x))) for x in [a,b]]
​
  if a+b==0: return "0"
  
  x=a+b
  while x%2==0:
    x//=2
    r-=1
  
  inter = x//2**r
  frac = x%2**r
  
  return str(inter)*bool(inter) + " "*(bool(inter) and bool(frac)) + (str(frac) + "/" + str(2**r))*bool(frac)

