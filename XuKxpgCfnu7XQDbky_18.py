
def sum_and_product(s, p):
  a,b,t=0,0,[]
  if s**2-4*p<0:
    return None
  else:
    a=round(((s**2-4*p)**(0.5)+s)/2,3)
    b=round((s-(s**2-4*p)**(0.5))/2,3)
    t=[a,b]
    return tuple(sorted(t))

