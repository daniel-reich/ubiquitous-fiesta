
def gcd(n1, n2):
  flag=1
  modd=n1
  while flag!=0:
    res1=n1%modd
    res2=n2%modd
    flag=res1+res2
    modd=modd-1
  return (modd+1)

