
def moran(n):
  su = sum(map(int,str(n)))
  pri = lambda x:all(x%i for i in range(2,x))
  return "H" if not n%su and not pri(int(n/su)) else "M" if pri(int(n/su)) else "Neither"

