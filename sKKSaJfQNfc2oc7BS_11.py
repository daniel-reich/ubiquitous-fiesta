
def sle(m):
  a,b,c = m[0]
  d,e,f = m[1]
  if b*d - a*e == 0:
    return False
  y = (c*d -a*f)/(b*d - a*e)
  x = (c-b*y)/a
  return (x,y)

