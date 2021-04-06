
def f(A, c):
  k=c**2+4*A
  l=c**2-4*A
  if l>0:
    return [round((k**0.5-l**0.5)/2,3), round((k**0.5+l**0.5)/2,3)]
  else:
    return "Does not exist"

