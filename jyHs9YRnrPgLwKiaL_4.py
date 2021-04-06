
import math
def split(x):
  k = math.ceil(x/2)+1
  r =  int(x/3)
  return max(round((x/i)**i,1) for i in range(r,k) if i!=0)

