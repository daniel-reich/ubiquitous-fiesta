
def circle_or_square(rad, area):
  import math 
  circumference_cir = 2*math.pi*rad
  perimeter_squ = (area**0.5)*4
  if circumference_cir > perimeter_squ:
    return True
  else:
    return False

