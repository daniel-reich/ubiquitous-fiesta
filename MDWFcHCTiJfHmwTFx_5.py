
def quadratic_equation(a,b,c):
  x1 = (-b + (b**2 - 4*a*c)**0.5)/(2*a)
  x2 = (-b - (b**2 - 4*a*c)**0.5)/(2*a)
  return int(x1) if x1>0 else int(x2)

