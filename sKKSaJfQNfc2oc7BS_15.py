
def sle(m):
  [[a,b,c], [d,e,f]] = m
  det = a*e-b*d
  if det == 0: return False
  x = (e*c-b*f)/det
  y = (a*f-c*d)/det
  return (x, y)

