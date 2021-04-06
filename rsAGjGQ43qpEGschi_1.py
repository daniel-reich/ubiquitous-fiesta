
def newton_raphson(c):
  a, b, c, d = c; x = 0
  f = 'a*x**3 + b*x**2 + c*x + d'
  f_prime = '3*a*x**2 + 2*b*x + c'
  
  for i in range(20):
    x = x - (eval(f)/eval(f_prime))
  return round(x,3)

