
def safecracker(start, inc):
  a = (start -inc[0])%100
  b = (a+inc[1])%100
  c = (b-inc[2])%100
  return [a,b,c]

