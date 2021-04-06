
def sum_and_product(s, p):
  D = s**2 - 4*p
  if D < 0:
    return None
  x = 1/2*(s - D**0.5)
  y = s - x
  return (round(x, 3), round(y, 3))

