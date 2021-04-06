
def quartic_equation(a,b,c):
  d=b*b-4*a*c
  l=[]
  if d>=0:
    x,y=(-b+d**.5)/2*a,(-b-d**.5)/2*a
    if x>=0:l+=[x**.5,-x**.5]
    if y>=0:l+=[y**.5,-y**.5]
    return len(set(l))
  return 0

