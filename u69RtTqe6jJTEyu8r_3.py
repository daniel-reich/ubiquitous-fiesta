
def impedance_calculator(Dd,Dc,er):
  import math
  return round(138*math.log(Dd/Dc, 10)/math.sqrt(er), 1)

