
def quadratic_equation(a, b, c):
  x = 1
  while (a * x**2) + (b*x) + c < 0:
    x += 1
  return x

