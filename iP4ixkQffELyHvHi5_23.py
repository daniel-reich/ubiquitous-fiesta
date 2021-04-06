
import math
​
def weight(r, h):
  vol = math.pi * r ** 2 * h 
  dm = round(vol * 0.001, 2)
  return dm

