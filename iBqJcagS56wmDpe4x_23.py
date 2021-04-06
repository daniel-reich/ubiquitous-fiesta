
import math
def vol_shell(r1, r2):
 if (round(4*math.pi*(r1*r1*r1-r2*r2*r2)/3,3))>=0:
   return (round(4*math.pi*(r1*r1*r1-r2*r2*r2)/3,3))
 else:
  return -1*(round(4*math.pi*(r1*r1*r1-r2*r2*r2)/3,3))

