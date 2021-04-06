
from math import sqrt, log10
​
def impedance_calculator(Dd, Dc, er):
  return round(138 * log10(Dd / Dc) / sqrt(er), 0)

