
import math
def circle_or_square(rad, area):
  circunference=2*math.pi*rad
  sq_perimeter=4*(area**0.5)
  
  if circunference>sq_perimeter:
    ans=True
  else:
    ans=False
    
  return ans

