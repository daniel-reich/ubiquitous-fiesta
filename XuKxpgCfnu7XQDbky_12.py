
import math 
def sum_and_product(s, p):
  if s**2-4*p<0:
    return None
  x=  (s+math.sqrt(s**2-4*p))/2
  y=s-x
  return (round(y,3),round(x,3))

