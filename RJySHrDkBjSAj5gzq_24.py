
def fac(n):
  return 1 if n<2 else n*fac(n-1)
def nespers(lst):
  p=fac(len(lst))
  for x in lst:
    if type(x)==list:
      p*=nespers(x)
    else:
      p*=1
  return p

