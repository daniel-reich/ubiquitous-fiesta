
def nespers(lst):
  r = 1
  for x in lst:
    if type(x) is list:
      r *= nespers(x)
  return r*fac(len(lst))
  
def fac(n):
  return 1 if n<1 else n*fac(n-1)

