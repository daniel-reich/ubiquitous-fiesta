
import math
def impedance_calculator(Dd, Dc, er):
  return round(59.93*math.log(Dd/Dc)/math.sqrt(er),1)

