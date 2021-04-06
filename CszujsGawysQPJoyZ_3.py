
import math
def hit_prince(vo, th, yo, ds):
  b = vo*math.sin(th*math.pi/180)
  t = (b+(b**2+2*9.81*yo)**.5)/9.81
  return abs(t*vo*math.cos(th*math.pi/180)-ds)<.5

