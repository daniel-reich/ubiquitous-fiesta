
import math
def cube_diagonal(volume):
  a=volume**(1./3.)
  return round(math.sqrt((math.sqrt(2)*a)*(math.sqrt(2)*a)+(a*a)),2)

