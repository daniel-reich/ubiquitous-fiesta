
step = 0.0001
def derive(function, value):
  result = (function(value + step) - function(value)) / step
  return float("%.3f" % result)
def newton_raphson(c):
  def f(x):
    fn = c[0]*x**3 + c[1]*x**2 + c[2]*x + c[3]    
    return fn
  x = 0.0
  while abs(f(x) / derive(f, x)) >= step: 
    x = x - f(x) / derive(f, x)
  return round(x, 3)

