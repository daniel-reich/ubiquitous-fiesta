
import math 
def vol_shell(r1, r2):
  return round((4/3) * math.pi * abs(r1 ** 3 - r2 ** 3), 3)

