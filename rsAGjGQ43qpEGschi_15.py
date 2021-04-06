
def newton_raphson(c):
  x=0.0
  for i in range(20):
    x=x-(c[0]*x**3+c[1]*x**2+c[2]*x+c[3])/(3*c[0]*x**2+2*c[1]*x+c[2])
  return round(x,3)

