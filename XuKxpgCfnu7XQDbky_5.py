
def sum_and_product(s, p):
  a = s**2 - 4*p
  if a<0: return None
  b = a**.5 / 2
  c = s/2
  x = c-b
  y = s-x
  return  (round(x, 3), round(y, 3))

