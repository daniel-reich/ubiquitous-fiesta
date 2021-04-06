
from math import log
​
def impedance_calculator(Dd, Dc, er):
  return round(138 * log(Dd/Dc, 10) / er**.5, 1)

