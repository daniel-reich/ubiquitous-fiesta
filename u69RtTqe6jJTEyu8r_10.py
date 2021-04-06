
def impedance_calculator(Dd, Dc, er):
  from math import log
​
  return round((138 * log((Dd/Dc), 10)) / (er ** .5),1)

