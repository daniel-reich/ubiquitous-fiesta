
def newton_raphson(coeff):
  a,b,c,d = coeff
  p = lambda x: a*x**3 + b*x**2 + c*x + d
  pd = lambda x: 3*a**3 + 2*b*x + c
  
  x=0
  for i in range(30):
    if abs(x)>10: x=9.532
    x = round(x-(p(x)/pd(x)),3)
  
  return round(x,3)

