
def gcd(a,b):
    return a if b==0 else gcd(b, a%b)
def binary_sum(lst):
  B=[x.split('.') for x in lst]
  d=max(len(x[1]) for x in B)
  for x in B:
    x[1]=x[1]+'0'*(d-len(x[1]))
  I=sum(int(x[0],2) for x in B)
  D=sum(int(x[1],2) for x in B)
  a,b=divmod(D, 2**d)
  n=I+a
  k=b//gcd(b,2**d)
  m=2**d//gcd(b, 2**d)
  if n==k==0:
    return '0'
  return '{}'.format(n)*(n>0)+' '*(n>0)*(k>0)+'{}/{}'.format(k, m)*(k>0)

