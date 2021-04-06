
from math import log10
def impedance_calculator(Dd, Dc, er):
  return round(138 * log10(Dd / Dc) / er ** 0.5, 1)

