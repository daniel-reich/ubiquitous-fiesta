
def gcd(n1, n2):
  x=set([a for a in range(1,n1+1) if n1%a==0])
  y=set([a for a in range(1,n2+1) if n2%a==0])
  return max(x&y)

