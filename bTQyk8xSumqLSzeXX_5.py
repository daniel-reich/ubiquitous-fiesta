
def has_valid_price(p):
  x=p and p.get('price',None)
  return 1 if type(x)in[int,float]and x>=0else 0

