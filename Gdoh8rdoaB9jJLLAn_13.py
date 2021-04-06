
def summation(exp, n):
  t = 0
  while n > 0:
    t += eval(exp)
    n -= 1
  return round(t, 1)

