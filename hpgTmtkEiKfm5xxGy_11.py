
def facto(n):
  return 1 if n==0 else n*facto(n-1)
def paths(x, y):
  return facto(x+y)//(facto(x)*facto(y))

