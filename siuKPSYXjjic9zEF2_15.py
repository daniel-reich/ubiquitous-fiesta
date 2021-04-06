
def foil(length):
  import math 
  w=4
  while length>=w*math.pi/2:
    length=length-w*math.pi
    w=w+0.005
  if length>0:
    w=w+0.0025
  return round(w,4)

