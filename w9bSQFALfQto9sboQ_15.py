
def gcd(n1, n2):
  l=[]
  for i in range(1,min(n1,n2)+1):
    if n1%i==0 and n2%i==0:
      l.append(i)
  return max(l)

