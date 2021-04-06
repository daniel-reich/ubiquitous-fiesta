
def sum_and_product(s,p):
  d=s*s/4-p
  if d<0:return None
  x,a=round(s/2+d**.5,3),round(s/2-d**.5,3)
  return min(a,x),max(a,x)

