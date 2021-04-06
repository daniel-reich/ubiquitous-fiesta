
import math
def red_area(r):
  return round(r*r-(.5*r*r*2.21429743-.5*r*r*math.sin(2.21429743))-(r*r-r*r*math.pi/4),3)

