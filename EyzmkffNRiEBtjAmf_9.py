
import math
def does_brick_fit(a,b,c, w,h):
  vol_b = a * b * c 
  vol_hole = math.pi * (w ** 2) * h 
  return vol_b <= vol_hole

