
import math
def split(x):
  max=x
  x=float(x)
  for i in range(2,int(x)):
    if((float(x/i))**i>max):
      max=float(x/i)**i
  if(math.floor(max)==math.ceil(max)):
    return int(max)
​
  return round(max,1)

