
def sum_and_product(s, p):
  q=s*s-4*p
  if q>=0:
    x=round((s-q**0.5)/2,3)
    y=round(s-x,3)
    return (x,y)

