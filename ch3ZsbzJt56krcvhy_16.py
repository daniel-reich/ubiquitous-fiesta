
def square_root(n):
  m,a,k=n,1,0
  while m>a:
    m//=2
    a*=2
    k+=1
  a=m+(a//2)
  while k:
    a=(a+n//a)//2
    k//=2
  return a

