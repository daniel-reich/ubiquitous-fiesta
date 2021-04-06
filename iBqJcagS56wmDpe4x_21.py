
import math as m
def vol_shell(r1, r2):
  vol = round(abs(4/3*m.pi*(r1**3 - r2**3)),3)
  return vol

