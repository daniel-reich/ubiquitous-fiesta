
from math import pi, sqrt, ceil
​
def foil(length):
  roll = ceil(sqrt(1600/pi * length + 2556801) - 1599)
  return 4 + 0.0025 * roll

