
def newton_raphson(c):
  f = lambda x: sum(a * x ** (3 - i) for i, a in enumerate(c))
  x = 0
  for i in range(20):
    x -= f(x) / (f(x + 1e-4) - f(x)) / 1e4
  return round(x, 3)

