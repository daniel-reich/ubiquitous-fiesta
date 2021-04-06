
from math import *
​
def weight(r, h):
  volume = pi * r * r * h
  volume /= 1000
  volume = round(volume, 2)
  return volume

