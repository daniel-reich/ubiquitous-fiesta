
def sum_and_product(s, p):
  b=s**2-4*p
  if b>=0:
    return (round((s-b**0.5)/2,3),round((s+b**0.5)/2,3))
  else:
    return None

