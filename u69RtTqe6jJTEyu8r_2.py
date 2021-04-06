
import math
​
def impedance_calculator(Dd,Dc,er):
  r = math.log(Dd/Dc, 10)
  den = math.sqrt(er)
  temp = (138 * r) / den
  return round(temp, 1)

