
def fractions(dec):
  pcs = dec.replace("(",".").replace(")",".").split(".")
  num = int(pcs[0]+pcs[1])*(10**len(pcs[2])-1) + int(pcs[2])
  den = 10**len(pcs[1]) * (10**len(pcs[2])-1)
  return simpfrac(num,den)
​
def gcd(n,m):
  while n>0:
    n,m = m%n,n
  return m
​
def simpfrac(n,m):
  r = gcd(n,m)
  return str(n//r) + "/" + str(m//r)

