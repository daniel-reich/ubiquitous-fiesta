
import math as m
​
​
def vol_shell(r1, r2):
  if r1 == r2:
    return 0
  else:
    volume = (4/3) * m.pi * (pow(r2,3) - pow(r1, 3))
    return abs(round(volume, 3))

