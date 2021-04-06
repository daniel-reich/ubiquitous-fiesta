
from fractions import*
def mixed_number(f):
  n,d=map(abs,map(int,f.split('/')))
  n,d=n//gcd(n,d),d//gcd(n,d)
  return'-'*(f[0]=='-')+(('%s %s/%s'%(n//d,n%d,d),'%s/%s'%(n,d))[n<d],str(n))[d==1]

