
def summation(exp, n):
  x = 0
  while n > 0:
    x += eval(exp)
    n -= 1
  return round(x,1)

