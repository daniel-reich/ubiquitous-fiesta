
import math as m
#def circle_or_square(rad, area):
# cp = 2*m.pi*rad
# qp = area ** 0.5 * 4
# return cp > qp
​
def circle_or_square(rad, area):
  cp = 2*m.pi*rad
  qp = m.sqrt(area)*4
  return cp > qp

