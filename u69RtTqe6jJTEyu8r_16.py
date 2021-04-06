
import math
def impedance_calculator(Dd, Dc, er):
  return round((138 * math.log(Dd/Dc,10)) / math.sqrt(er))

