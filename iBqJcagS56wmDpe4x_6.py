
import math
​
def vol_shell(r1, r2):
  if r2>r1: r1,r2=r2,r1
  return round(((4*math.pi)*(r1**3-r2**3)/3),3)

