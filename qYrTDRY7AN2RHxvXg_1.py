
def f(A,c):
  d=c**4-16*A*A
  if d<0:return'Does not exist'
  b=((c*c+d**.5)/2)**.5
  return sorted([round(2*A/b,3),round(b,3)])

