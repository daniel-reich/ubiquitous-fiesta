
def sum_and_product(s, p):
  d = s**2 - 4*p
  if d<0: return None
  return (round((s-d**.5)/2,3),round((s+d**.5)/2,3))

