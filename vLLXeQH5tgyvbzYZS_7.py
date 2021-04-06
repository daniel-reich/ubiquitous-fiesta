
def coprime(a, b):
  while b:
    a, b = b, a % b
  return a == 1
    
def is_prim_pyth_triple(lst):
  a,b,c = lst
  if a**2 + b**2 + c**2 == 2 * (max(lst)**2):
    return coprime(a, b) and coprime(b, c) and coprime(a, c)
  else:
    return False

