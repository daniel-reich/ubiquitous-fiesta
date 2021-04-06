
def gcd(a,b):
  while b>0:
    a,b=b,a%b
  return a
def lcm_of_list(l):
  m=l[0]
  for i in l[1:]:
    m=m*i//gcd(m,i)
  return m

