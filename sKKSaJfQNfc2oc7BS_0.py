
def sle(m):
  a,b,c,d,e,f = m[0]+m[1]
  if b*d==a*e: return False
  x = (b*f-c*e)/(b*d-a*e)
  return (x, (-a*x+c)/b)

