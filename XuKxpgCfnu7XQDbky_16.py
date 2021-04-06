
def sum_and_product(s, p):
  if s == 0 and p == 0: return 0,0
  a , b , c = 1 , -s , p
  x = (-b - (b**2 - 4*a*c)**0.5)/2*a
  y = s - x
  if type(x) == complex: return None
  return round(x,3), round(y,3)

