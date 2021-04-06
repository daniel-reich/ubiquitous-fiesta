
def sum_and_product(s, p):
  if s**2 < 4*p:
    return None
  x1 = (s + (s*s - 4*p)**.5)/2
  x2 = (s - (s*s - 4*p)**.5)/2
  x = round(min(x1,x2),3)
  y = round(s-x,3)
  return (x,y)

