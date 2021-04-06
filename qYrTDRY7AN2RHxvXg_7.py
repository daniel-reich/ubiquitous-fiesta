
def f(A,c):
  disc = c**4 - 16*A**2
  if disc<0:
    return "Does not exist"
  a = ((c**2 - disc**.5)/2)**.5
  return [round(a,3), round(2*A/a,3)]

