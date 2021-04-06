
import math
def weight(r, h):
  volume = math.pi * (r**2) * h
  dm = volume / 1000
  return round(dm, 2)

