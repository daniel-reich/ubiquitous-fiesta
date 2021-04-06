
from math import log 
​
def impedance_calculator(Dd, Dc, er):
  return round(log(Dd / Dc, 10) * 138 / er ** 0.5)

